import streamlit as st
import pandas as pd
from utils.db import get_engine

engine = get_engine()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.title("Filtres")

agence = st.sidebar.selectbox("Agence", ["All"])
segment = st.sidebar.selectbox("Segment", ["All", "Premium", "Standard", "Risqué"])
annee = st.sidebar.slider("Année", 2022, 2024, (2022, 2024))

# =========================
# KPI QUERY
# =========================
kpi_query = """
SELECT
    COUNT(transaction_id) AS total_transactions,
    SUM(montant) AS total_ca,
    COUNT(DISTINCT client_id) AS clients_actifs,
    AVG(montant) AS marge_moyenne
FROM transactions
WHERE statut = 'Completed'
"""

df_kpi = pd.read_sql(kpi_query, engine)

# =========================
# TITLE
# =========================
st.title("📊 Vue Exécutive")

# =========================
# KPI CARDS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Transactions", int(df_kpi["total_transactions"][0]))
col2.metric("💰 CA Total", f"{df_kpi['total_ca'][0]:,.2f}")
col3.metric("👤 Clients actifs", int(df_kpi["clients_actifs"][0]))
col4.metric("📉 Marge moyenne", f"{df_kpi['marge_moyenne'][0]:.2f}")

# =========================
# DATA QUERY (FIXED)
# =========================
data_query = f"""
SELECT
    t.montant,
    t.type_operation,
    t.date_transaction,
    c.client_id,
    c.score_credit_client,
    CASE 
        WHEN c.score_credit_client >= 700 THEN 'Premium'
        WHEN c.score_credit_client >= 500 THEN 'Standard'
        ELSE 'Risqué'
    END AS segment,
    a.nom_agence,
    p.nom_produit
FROM transactions t
JOIN client c ON t.client_id = c.client_id
LEFT JOIN agence a ON t.agence_id = a.agence_id
LEFT JOIN produit p ON t.produit_id = p.produit_id
WHERE EXTRACT(YEAR FROM t.date_transaction) BETWEEN {annee[0]} AND {annee[1]}
"""

df = pd.read_sql(data_query, engine)

df["date_transaction"] = pd.to_datetime(df["date_transaction"])
df["year_month"] = df["date_transaction"].dt.to_period("M").astype(str)

# =========================
# FILTER LOGIC SAFE
# =========================
if segment != "All":
    df = df[df["segment"] == segment]

if agence != "All" and "nom_agence" in df.columns:
    df = df[df["nom_agence"] == agence]

# =========================
# 1. LINE CHART
# =========================
st.subheader("📈 Évolution mensuelle (Débits / Crédits)")

monthly = df.groupby(["year_month", "type_operation"])["montant"].sum().unstack().fillna(0)

st.line_chart(monthly)

# =========================
# 2. BAR CHART AGENCE
# =========================
st.subheader("🏦 CA par agence")

if "nom_agence" in df.columns:
    ca_agence = df.groupby("nom_agence")["montant"].sum().sort_values(ascending=False)
    st.bar_chart(ca_agence)
else:
    st.warning("Colonne agence indisponible")

# =========================
# 3. BAR CHART PRODUIT
# =========================
st.subheader("💳 CA par produit bancaire")

if "nom_produit" in df.columns:
    ca_produit = df.groupby("nom_produit")["montant"].sum().sort_values(ascending=False)
    st.bar_chart(ca_produit)
else:
    st.warning("Colonne produit indisponible")

# =========================
# 4. PIE CHART SEGMENT
# =========================
st.subheader("🥧 Répartition des clients par segment")

segment_dist = df["segment"].value_counts()
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.pie(segment_dist, labels=segment_dist.index, autopct="%1.1f%%")
ax.axis("equal")

st.pyplot(fig)