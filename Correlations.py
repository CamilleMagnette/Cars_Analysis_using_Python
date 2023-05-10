# Contents of ~/my_app/pages/page_2.py
import streamlit as st

st.markdown("# Analyse de corrélation")
st.sidebar.markdown("# Corrélation 🔦")

# Importer le dataframe
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)
df_voitures['continent'] = df_voitures['continent'].str.replace('.', '')

# Ajouter des boutons pour filtrer par région dans le bandeau de gauche
list_continent = df_voitures['continent'].unique()
st.sidebar.subheader('Sélectionner une région')
selected_region = st.sidebar.selectbox('', list_continent)
#selected_region = st.sidebar.multiselect(label = 'Sélectionner une région', options = list_continent)
df_selected_region = df_voitures[df_voitures['continent'] == selected_region]

st.write("Nous pouvons observer des corrélation positives entre la puissance des véhicules (hp), leur masse (weightlbt) le cylindre (cylinders) et la taille de leur moteur (cubicinches).")
st.write("Nous pouvons également observer des corrélation négatives entre la consommation (mpg), leur masse (weightlbt) le cylindre (cylinders) et la taille de leur moteur (cubicinches).")

# CREER DES TAB 
tab1, tab2, tab3, tab4 = st.tabs(['HEATMAP', 'PAIRPLOT', 'CORRELATION POSITIVE', 'CORRELATION NEGATIVE'])


# TRAVAILLER SUR LES TAB 

with tab1 : 

    # Retravailler le dataframe
    df_selected_region['continent'] = df_selected_region['continent'].factorize()[0]
    st.subheader('Heatmap')

    # Réaliser une heatmap
    import seaborn as sns
    import matplotlib.pyplot as plt

    correlation = df_selected_region.corr()
    fig, ax = plt.subplots()

    viz_correlation = sns.heatmap(correlation, annot= True, center=0, cmap = sns.color_palette("vlag", as_cmap=True))
    st.pyplot(viz_correlation.figure)
    #sns.heatmap(correlation, annot=True, ax=ax,vmax=1, vmin=-1, cmap='coolwarm' )
    #st.pyplot(fig)

    
with tab2 : 
    
    st.subheader('Pairplot')
    
    # Réaliser un Pairplot    
    import matplotlib.pyplot as plt
    import seaborn as sns  
    fig, ax = plt.subplots()
    #st.title("Hello") 
    fig = sns.pairplot(df_selected_region, hue = 'year')   
    st.pyplot(fig)
    
with tab3 : 

    st.subheader('HP & WEIGHTLBS')

    # Réaliser un nuage de point
    import matplotlib.pyplot as plt
    import seaborn as sns  
    fig, ax = plt.subplots()
    sns.regplot(x= df_selected_region['hp'], y= df_selected_region['weightlbs'], ax=ax)
    #ax.scatter(x= df_selected_region['hp'], y= df_selected_region['weightlbs'], label = "hp&weightlbs")
    #plt.title("HP & WEIGHTLBS")
    plt.xlabel("HP")
    plt.ylabel("WEIGHTLBS")
    #plt.legend()
    st.pyplot(fig)
    
    
with tab4 : 
    
    st.subheader('MPG & WEIGHTLBS')

    # Réaliser un nuage de point
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    sns.regplot(x= df_selected_region['mpg'], y= df_selected_region['weightlbs'], ax=ax)
    #ax.scatter(x= df_selected_region['mpg'], y= df_selected_region['weightlbs'], label = "mpg&weightlbs")
    #plt.title("MPG&weightlbs")
    plt.xlabel("MPG")
    plt.ylabel("WEIGHTLBS")
    #plt.legend()
    st.pyplot(fig)
    