import pandas as pd 
import streamlit as st
import numpy as np

st.title('Zeitleiste')

# Container für die Zeitleiste
st.markdown("### Zeitleiste")

# Erzeuge die Jahre von -4000 bis 2050
years = list(range(-4000, 2051, 50))  # alle 50 Jahre zur besseren Übersicht

# Erzeuge HTML-Elemente für die Zeitleiste
timeline_html = "<div style='white-space: nowrap; overflow-x: auto; padding: 10px; border-bottom: 2px solid #ccc;'>"
for year in years:
    timeline_html += f"<span style='display: inline-block; width: 80px; text-align: center;'>{year}</span>"
timeline_html += "</div>"

# Zeige die Zeitleiste mit HTML
st.markdown(timeline_html, unsafe_allow_html=True)