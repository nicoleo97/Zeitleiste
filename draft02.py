import streamlit as st
import pandas as pd

st.title("Zeitleiste")

tab16, tab17, tab18, tab19, tab20, tab21 = st.tabs(['16.Jhdt.', '17.Jhdt.', '18.Jhdt.', '19.Jhdt.', '20.Jhdt.', '21.Jhdt.'])



# Rahmen der Jahrhunderte aus CSV laden
jhdt_df = pd.read_csv('background_data/jahrhundert.txt', sep=',')

# Main Events aus CSV laden
events_df = pd.read_csv('data/events.csv', sep=',')



optionen = events_df['Fach'].unique()
with st.sidebar:
    st.header("Fächerauswahl")
    for fach in optionen:
        st.checkbox(fach, value=True, key=fach)
auswahl =  []
for fach in optionen:
    if st.session_state.get(fach, True):
        auswahl.append(fach)

events_df = events_df[events_df['Fach'].isin(auswahl)]


# Funktionen
def Header(jhdt,anfang,ende):
    st.header(f"{jhdt}")
    st.write(f'{anfang} - {ende}')
    genau = st.checkbox('Nach Jahr filtern', value=True,key=anfang)
    if genau:
        jahreszahl = st.select_slider('',options=(range(anfang,ende+1,1)),value=anfang+15)
    

def Badge_Fach(fach):
    if fach == 'Mathe':
        st.badge('MATHE',color='blue')
    elif fach == 'Physik':
        st.badge('PHYSIK', color='orange')
    else:
        st.badge(fach, color='gray')

def Filter(events_df,anfang,ende):
    if genau:
        df_filt = events_df[events_df['Jahr'] == jahreszahl]
    else:
        df_filt = events_df[events_df['Jahr'] >= anfang]
        df_filt = df_filt[df_filt['Jahr'] <= ende]
    return df_filt

def Inputs(events_df):
    for event in events_df.itertuples():
        st.subheader(f"{event.Jahr} - {event.Ereignis}")
        st.write(event.Infotext)
        Badge_Fach(event.Fach)
        st.divider()


# Verwaltung von Tabs
with tab21:
    Header(jhdt_df['Bezeichnung'][0], jhdt_df['Anfang'][0], jhdt_df['Ende'][0])
    Inputs(Filter(events_df, jhdt_df['Anfang'][0], jhdt_df['Ende'][0]))

with tab20:
    Header(jhdt_df['Bezeichnung'][1], jhdt_df['Anfang'][1], jhdt_df['Ende'][1])
    Inputs(Filter(events_df, jhdt_df['Anfang'][1], jhdt_df['Ende'][1]))
with tab19:
    Header(jhdt_df['Bezeichnung'][2], jhdt_df['Anfang'][2], jhdt_df['Ende'][2])
    Inputs(Filter(events_df, jhdt_df['Anfang'][2], jhdt_df['Ende'][2])) 

with tab18:
    Header(jhdt_df['Bezeichnung'][3], jhdt_df['Anfang'][3], jhdt_df['Ende'][3])
    Inputs(Filter(events_df, jhdt_df['Anfang'][3], jhdt_df['Ende'][3]))

with tab17:
    Header(jhdt_df['Bezeichnung'][4], jhdt_df['Anfang'][4], jhdt_df['Ende'][4])
    Inputs(Filter(events_df, jhdt_df['Anfang'][4], jhdt_df['Ende'][4])) 

with tab16:
    Header(jhdt_df['Bezeichnung'][5], jhdt_df['Anfang'][5], jhdt_df['Ende'][5])
    Inputs(Filter(events_df, jhdt_df['Anfang'][5], jhdt_df['Ende'][5]))
