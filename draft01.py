import streamlit as st
import pandas as pd

data = pd.read_csv('data/test.csv')



auswahl_dict = {-4000:'4000 v. Chr.',
                -3000:'3000 v. Chr.',
                -2000:'2000 v. Chr,',
                -1000:'1000 v. Chr.',
                -500:'500 v. Chr.',
                0:'Zeitwende',
                500:'500 n. Chr.',
                1000:'1000 n. Chr.',
                1500:'16. Jhdt.',
                1600:'17. Jhdt.',
                1700:'18. Jhdt.',
                1800:'19. Jhdt.',
                1900:'20. Jhdt.',
                2000:'21. Jhdt.'}

reverse_auswahl_dict = {v: k for k, v in auswahl_dict.items()}

auswahl_texte = list(auswahl_dict.values())
auswahl_zahl = list(auswahl_dict.keys())

auswahl = st.select_slider('Wähle einen Zeitraum',options=auswahl_texte, value='20. Jhdt.')

st.header(auswahl)
st.subheader(f"{reverse_auswahl_dict[auswahl]+1} bis {reverse_auswahl_dict[auswahl]+100}")

