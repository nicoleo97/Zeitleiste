import streamlit as st
import pandas as pd
import plotly.express as px

# Daten laden
df = pd.read_csv("events.csv")

# Fächer dynamisch auf x-Werte mappen
unique_faecher = df['Fach'].unique()
fach_map = {fach: i+1 for i, fach in enumerate(unique_faecher)}
df['x'] = df['Fach'].map(fach_map)

# Plot erstellen
fig = px.scatter(
    df,
    x="x",
    y="Jahr",
    text="Ereignis",
    hover_data=["Ereignis", "Infotext", "Fach", "Jahr"]
)

fig.update_traces(textposition='top center')
fig.update_layout(
    yaxis=dict(autorange="reversed", title="Jahr"),
    xaxis=dict(
        title="Fach",
        tickvals=list(fach_map.values()),
        ticktext=list(fach_map.keys())
    ),
    height=800
)

st.plotly_chart(fig, use_container_width=True)
