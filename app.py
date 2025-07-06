import pandas as pd 
import streamlit as st
import numpy as np

st.title('Zeitleiste')


###########################################################
# JAHRHUNDERT AUSWAHL
century = list(range(-4000,2200,100))

century_slider = st.select_slider('Jahrhundert',options=century,value=2000)

if 0 < century_slider <= 1500:
    act_label = str(abs(century_slider))
    act_cent = st.container()
    act_cent.header(f"{act_label} n. Chr.")

elif century_slider == 0:
    act_cent.title("Zeitwende")

elif century_slider < 0:
    act_label = str(abs(century_slider))
    act_cent = st.container()
    act_cent.header(f"{act_label} v. Chr.")

elif century_slider > 1500:
    act_label = str(abs(century_slider))
    act_cent = st.container()
    act_cent.header(f"{act_label}er Jahre")

###########################################################

data = pd.read_csv('data/test.csv', sep=',')

start = century_slider 
ende = century_slider + 100
filter = list(range(start,ende))

data_filtered = data[data['jahr'].isin(filter)]
st.write(data_filtered)