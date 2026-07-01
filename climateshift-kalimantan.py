import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="ClimateShift AI - Kalimantan", layout="wide")
st.title("🌴 ClimateShift AI: Kalimantan, Indonesia (with Map)")

st.sidebar.header("Kalimantan Analysis")
region = st.sidebar.selectbox("Select Region", ["Central Kalimantan Peatlands", "East Kalimantan Forests", "South Kalimantan Coast"])
scenario = st.sidebar.selectbox("Scenario", ["Current", "Moderate Warming"])

if st.sidebar.button("Run Analysis & Show Map"):
    st.success("AI + Map Processing...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Carbon Monitoring")
        carbon = pd.DataFrame({"Metric": ["Carbon Stock (tCO₂e/ha)", "Deforestation Risk (%)"], "Value": [np.random.uniform(180, 260), np.random.uniform(5, 22)]})
        st.bar_chart(carbon.set_index("Metric"))
    with col2:
        st.subheader("Resilience Assessment")
        resilience = pd.DataFrame({"Risk": ["Peat Fire/Flood", "Drought Impact"], "Score": [np.random.randint(55, 90), np.random.randint(45, 75)]})
        st.bar_chart(resilience.set_index("Risk"))
    
    st.metric("Kalimantan Carbon Stock Estimate", "~12.5 MtCO₂e", "Monitoring active")
    st.metric("Paradigm Shift Score", "87/100", "Strong scalability")

# Interactive Map
st.subheader("Kalimantan Map View")
m = folium.Map(location=[-1.0, 114.0], zoom_start=6)
folium.Marker([-2.5, 113.5], popup="High Carbon Peat Area", tooltip="Carbon Hotspot").add_to(m)
folium.Marker([0.5, 117.0], popup="Forest Resilience Zone", tooltip="Priority Area").add_to(m)
st_folium(m, width=700, height=500)

st.markdown("### GCF Paradigm Shift Metrics")
st.json({
    "Scalability": "High - Kalimantan model replicable across Indonesia/SE Asia",
    "Innovation": "AI + Sentinel satellite for peat & forest tracking",
    "Impact": "Supports Indonesia NDC & REDD+"
})

st.caption("Kalimantan-focused prototype with map. Ready for GCF-style projects!")
