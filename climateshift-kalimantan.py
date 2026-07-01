import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="ClimateShift AI - Kalimantan", layout="wide")
st.title("🌴 ClimateShift AI: Kalimantan Focus")
st.markdown("**Early-stage GCF-aligned prototype for Borneo carbon & resilience**")

st.sidebar.header("Kalimantan Parameters")
region = st.sidebar.selectbox("Select Kalimantan Region", ["Central Kalimantan Peatlands", "East Kalimantan Forests", "South Kalimantan Coast"])
scenario = st.sidebar.selectbox("Scenario", ["Current", "Moderate Warming"])

if st.sidebar.button("Run AI Analysis for Kalimantan"):
    st.success("Processing Satellite + AI Data (Prototype)...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Carbon Monitoring (Kalimantan Forests)")
        carbon = pd.DataFrame({"Metric": ["Carbon Stock", "Deforestation Risk"], "Value": [np.random.uniform(200, 280), np.random.uniform(8, 18)]})
        st.bar_chart(carbon.set_index("Metric"))
    with col2:
        st.subheader("Resilience Assessment")
        resilience = pd.DataFrame({"Risk": ["Flood/Peat Fire", "Drought"], "Score": [np.random.randint(50, 85), np.random.randint(40, 70)]})
        st.bar_chart(resilience.set_index("Risk"))
    
    st.metric("Estimated Carbon in Selected Area", "8.4 MtCO₂e", "↓ 1.2% last year")
    st.metric("Paradigm Shift Score", "85/100", "High potential for scalable MRV in Indonesia")

st.markdown("### GCF Paradigm Shift Metrics")
st.json({
    "Scalability": "High - Kalimantan model replicable across Indonesia/SE Asia",
    "Innovation": "AI + Sentinel satellite for peat & forest tracking",
    "Impact": "Supports Indonesia NDC & REDD+"
})

st.caption("Kalimantan-focused prototype. Real version would use Google Earth Engine for live satellite data.")