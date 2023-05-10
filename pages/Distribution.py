# Contents of ~/my_app/pages/page_3.py
import streamlit as st

st.markdown("# Analyse de distribution")
st.sidebar.markdown("# Distribution 🔎")

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
df_selected_region = df_selected_region.drop('year', axis = 1)

# Afficher les statistiques sur le jeu de données global
st.sidebar.subheader('Global statistics')
df2=df_voitures.drop('year', axis = 1)
st.sidebar.dataframe(df2.describe())


st.subheader('Répartition des données')

#st.write("Sur 261 véhicules, 125 sont en 4 cylindres ( 47,89 % ) , 55 en 6 cylindres (21 % ) et 76 en 8 cylindres (29 %)")
#st.write("Si la moyenne des tailles des moteurs est à 3291 cm³, c'est parce qu'il y a un fort déséquilibre entre les véhicules de la région US par rapport aux régions Japan et Europe.")
#st.write("Si les véhicules japonais sont souvent bien moins gourmands que la moyenne, les records de consommation se trouvent encore du côté de la région US")
#st.write("Enfin, il serait très intéressant d'avoir un plus grand jeu de données sur des véhicules plus récents afin de vérifier si nos prédictions de baisse de consommation sont réalisées.")


# CREER DES TAB 

tab1, tab2 = st.tabs(['DIAGRAM PER CONTINENT', 'STATISTICS PER CONTINENT'])



# TRAVAILLER SUR LES TAB 

with tab1 : 

    # Mettre en place un menu déroulant 
    list_variables = list(['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year', 'continent'])
    choix = st.selectbox("variables : ",list_variables)

    # Réaliser un diagram en barre 
    import matplotlib.pyplot as plt
    x = df_selected_region[choix]
    fig, ax = plt.subplots()
    ax.hist(x,  bins=9, color='cornflowerblue', rwidth=0.8)
    st.pyplot(fig)

with tab2 : 

    # Afficher les données statistiques 
    describe = df_selected_region.describe() 
    st.write(describe)

