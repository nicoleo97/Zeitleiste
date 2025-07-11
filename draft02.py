import streamlit as st
import pandas as pd

#with st.sidebar:
 #   kee = st.text_input('Password?')
  #  if kee != '7B':
   #     st.error('Falsches Passwort!')
    #    st.stop()




st.title("Zeitleiste")

tab16, tab17, tab18, tab19, tab20, tab21, input_tab = st.tabs(['16.Jhdt.', '17.Jhdt.', '18.Jhdt.', '19.Jhdt.', '20.Jhdt.', '21.Jhdt.','Input'])



# Rahmen der Jahrhunderte aus CSV laden
jhdt_df = pd.read_csv('background_data/jahrhundert.txt', sep=',')

# Main Events aus CSV laden
events_df = pd.read_csv('data/events.csv', sep=',')
events_df = events_df.sort_values(by=['Jahr'], ascending=True)

# Sidebar für Fächerfilter
auswahl_fach = ['Mathe', 'Physik', 'Deutsch','Latein', 'Geschichte', 'BE', 'Musik', 'Other']
with st.sidebar:
    st.header("Fächerauswahl")
    for fach in auswahl_fach:
        st.checkbox(fach, value=True, key=fach)
auswahl =  []
for fach in auswahl_fach:
    if st.session_state.get(fach, True):
        auswahl.append(fach)

events_df = events_df[events_df['Fach'].isin(auswahl)]




# Funktionen
def Header(jhdt,anfang,ende):
    st.header(f"{jhdt}")
    st.write(f'{anfang} - {ende}')
   
    
def Badge_Fach(fach):
    if fach == 'Mathe':
        st.badge('MATHE',color='blue')
    elif fach == 'Physik':
        st.badge('PHYSIK', color='orange')
    elif fach == 'Deutsch':
        st.badge('DEUTSCH', color='red')
    elif fach == 'Latein':
        st.badge('LATEIN', color='red')
    elif fach == 'Geschichte':
        st.badge('GESCHICHTE', color='green')
    elif fach == 'BE':
        st.badge('KUNST', color='violet')
    elif fach == 'Musik':
        st.badge('MUSIK', color='violet')    
    else:
        st.badge(fach, color='gray')

def Genauigkeit():
    genau = st.checkbox('Nach exakten Jahren filtern', value=False,key='genau')
    if genau:
        jahreszahl = st.select_slider('',options=range(anfang,ende,1),key='jahreszahl')
        anfang = jahreszahl
        ende = jahreszahl
 


def Filter(events_df,anfang,ende):
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
with input_tab:
    input_form = st.form('Neuer Eintrag')
    input_form.header('Neuen Eintrag hinzufügen')
    input_jahr = input_form.number_input('Jahr', min_value=1501, max_value=2100, step=1, value=1997,help='Erreignisse vor der Zeitwende mit Minus eingeben, z.B. -500 für 500 v.Chr.')
    input_fach = input_form.selectbox('Fach', options=auswahl_fach, help='Zuordnung zu einem Unterrichtsfach',index=2)
    input_ereignis = input_form.text_input('Ereignis', help='Kurze Bezeichnung des Ereignisses, z.B. "Erfindung des Buchdrucks"')
    input_infotext = input_form.text_area('Infotext', help='Längere Beschreibung des Ereignisses, z.B. "Johannes Gutenberg erfindet den Buchdruck mit beweglichen Lettern"')
    sender = input_form.form_submit_button('Vorschlag abschicken')

    if sender:
        # Neuen Eintrag in die CSV-Datei schreiben
        new_event = pd.DataFrame({
            'Jahr': [input_jahr],
            'Fach': [input_fach],
            'Ereignis': [input_ereignis],
            'Infotext': [input_infotext]
        })
        new_event.to_csv('data/inputs.csv', mode='a', header=False, index=False)
        st.success('Neuer Eintrag erfolgreich abgeschickt!')


with tab21:
    anfang = jhdt_df['Anfang'][0]
    ende = jhdt_df['Ende'][0]
    Header(jhdt_df['Bezeichnung'][0], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][0], jhdt_df['Ende'][0]))

with tab20:
    anfang = jhdt_df['Anfang'][1]
    ende = jhdt_df['Ende'][1]
    Header(jhdt_df['Bezeichnung'][1], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][1], jhdt_df['Ende'][1]))

with tab19:
    anfang = jhdt_df['Anfang'][2]
    ende = jhdt_df['Ende'][2]
    Header(jhdt_df['Bezeichnung'][2], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][2], jhdt_df['Ende'][2])) 

with tab18:
    anfang = jhdt_df['Anfang'][3]
    ende = jhdt_df['Ende'][3]
    Header(jhdt_df['Bezeichnung'][3], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][3], jhdt_df['Ende'][3]))

with tab17:
    anfang = jhdt_df['Anfang'][4]
    ende = jhdt_df['Ende'][4]
    Header(jhdt_df['Bezeichnung'][4], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][4], jhdt_df['Ende'][4])) 

with tab16:
    anfang = jhdt_df['Anfang'][5]
    ende = jhdt_df['Ende'][5]
    Header(jhdt_df['Bezeichnung'][5], anfang, ende)
    Inputs(Filter(events_df, jhdt_df['Anfang'][5], jhdt_df['Ende'][5]))
