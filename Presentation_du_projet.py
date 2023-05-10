# Contents of ~/my_app/main_page.py
import streamlit as st


st.set_page_config(
    page_title="Cars dataset analysis",
    layout="wide",
    page_icon=":🚙:")

st.markdown("# DATASET")
st.sidebar.markdown("# DATASET PER REGION 🚙 ")

st.subheader('Réaliser une étude de corrélation et de distribution sur la base du dataset ci-dessous')


# Importer le dataframe
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)
df_voitures['continent'] = df_voitures['continent'].str.replace('.', '')

# Ajouter des boutons pour filtrer par région dans le bandeau de gauche
list_continent = df_voitures['continent'].unique()
st.sidebar.subheader('Sélectionner une région')
selected_region = st.sidebar.selectbox(' ', list_continent)
df_selected_region = df_voitures[df_voitures['continent'] == selected_region]

# Afficher le dataframe
st.write(df_selected_region)




