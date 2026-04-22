import streamlit as st

st.set_page_config(
    page_title="FinanceCore Dashboard",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("📊 FinanceCore Dashboard")

st.markdown("Sélectionnez une page dans la barre latérale 👇")

# =========================
# SIDEBAR MENU
# =========================
menu = {
    "🏠 Accueil": "home",
    "📊 Vue Exécutive": "executive",
    "⚠️ Analyse Risque": "risk"
}

