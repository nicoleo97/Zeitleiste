import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

fach =['Mathe','Physik','Chemie']


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
start = reverse_auswahl_dict[auswahl]+1
ende = reverse_auswahl_dict[auswahl]+100
st.subheader(f"{start} bis {ende}")


data_mathe = pd.read_csv('data/mathe.csv')
st.write(data_mathe)
data_mathe["x"] = 1

fig, ax = plt.subplots()
ax.scatter(data_mathe["x"],data_mathe["Jahr"])

st.pyplot(fig)