import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from utils.db import get_engine

engine = get_engine()

df = pd.read_sql("""
SELECT score_credit_client, montant, is_anomaly
FROM transactions t
JOIN client c ON t.client_id = c.client_id
""", engine)
st.sidebar.title("Filtres")

agence = st.sidebar.selectbox("Agence", ["All"])
segment = st.sidebar.selectbox("Segment", ["All", "Premium", "Standard", "Risqué"])
annee = st.sidebar.slider("Année", 2022, 2024, (2022, 2024))
corr = df.corr(numeric_only=True)

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.title("📊 Analyses de Risques")
st.subheader("🔥 Heatmap Risque")
st.pyplot(fig)
fig2, ax2 = plt.subplots()
st.subheader("🔥  score crédit vs montant transaction")

ax2.scatter(df["score_credit_client"], df["montant"], c=df["is_anomaly"])
ax2.set_xlabel("Score crédit")
ax2.set_ylabel("Montant")

st.pyplot(fig2)
st.subheader("👥 Top 10 clients")
top_risk = pd.read_sql("""
SELECT 
    t.client_id,
    c.score_credit_client,
    SUM(t.montant) AS total
FROM transactions t
JOIN client c 
    ON t.client_id = c.client_id
GROUP BY 
    t.client_id, 
    c.score_credit_client
ORDER BY 
    c.score_credit_client ASC, 
    total DESC
LIMIT 10;
""", engine)

st.dataframe(top_risk)