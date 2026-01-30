import streamlit as st
import requests

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
# ✈️ Flight Delay Prediction Dashboard  
### Spark MLlib • Flask API • Streamlit Interface
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧠 Modèle ML", "Spark MLlib")

with col2:
    st.metric("⚙️ Backend API", "Flask")

with col3:
    st.metric("🟢 Statut", "En ligne")

st.divider()

st.subheader("📊 Prédire le retard (compagnie AA)")

st.info("Entrez les valeurs des autres compagnies pour estimer le retard de **AA**.")


c1, c2, c3 = st.columns(3)

with c1:
    month = st.number_input("📅 Month", 1, 12, 6)

    AS = st.number_input("Alaska Airlines (AS)", 0.0)
    B6 = st.number_input("JetBlue Airways (B6)", 0.0)

with c2:
    DL = st.number_input("Delta Air Lines (DL)", 0.0)
    EV = st.number_input("ExpressJet (EV)", 0.0)
    F9 = st.number_input("Frontier Airlines (F9)", 0.0)
    HA = st.number_input("Hawaiian Airlines (HA)", 0.0)

with c3:
    MQ = st.number_input("Envoy Air (MQ)", 0.0)
    NK = st.number_input("Spirit Airlines (NK)", 0.0)
    OO = st.number_input("SkyWest Airlines (OO)", 0.0)
    UA = st.number_input("United Airlines (UA)", 0.0)
    US = st.number_input("US Airways (US)", 0.0)
    VX = st.number_input("Virgin America (VX)", 0.0)
    WN = st.number_input("Southwest Airlines (WN)", 0.0)

st.markdown("<br>", unsafe_allow_html=True)
predict_col = st.columns([4, 2, 4])[1]
with predict_col:
    predict_btn = st.button("🚀 Prédire le retard")
if predict_btn:

    payload = {
        "Month": month,
        "AS": AS,
        "B6": B6,
        "DL": DL,
        "EV": EV,
        "F9": F9,
        "HA": HA,
        "MQ": MQ,
        "NK": NK,
        "OO": OO,
        "UA": UA,
        "US": US,
        "VX": VX,
        "WN": WN,
    }

    with st.spinner("⏳ Calcul en cours..."):
        try:
            r = requests.post(
                "http://127.0.0.1:5001/predict",
                json=payload
            )

            if r.status_code == 200:
                pred = r.json()["prediction"]

                st.success(f"⏱️ **Retard prédit pour AA : {pred:.2f} minutes**")

            else:
                st.error(r.text)

        except Exception as e:
            st.error(f"Erreur API Flask : {e}")

# ---------------- FOOTER ----------------
st.divider()

st.caption("Mini-projet Big Data — Mohamed Baounna — Spark • Flask • Streamlit")
