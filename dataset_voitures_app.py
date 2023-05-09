
# Créer un dossier local avec notre projet et un nouveau fichier dataset_voitures_app.py avec les deux lignes suivantes
import streamlit as st
st.title('Hello Wilders, welcome to my application!')

# Lancer dans le terminal
# Se placer dans le dossier qui contient le script, et lancer la commande suivante :
# streamlit run dataset_voitures_app.py.py
# Le navigateur va automatiquement ouvrir un nouvelle page streamlit 

"""
REALISER : 
une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.
des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
l'application doit être disponible sur la plateforme de partage.
Publie ensuite ici le lien de ton application. 
Le lien doit ressembler à https://share.streamlit.io/wilder/streamlit_app/my_streamlit_app.py.
"""

# Créer des tab
tab1, tab2, tab3 = st.tabs(['DATA', 'HEATMAP', 'DISTRIBUTION'])

# Importer le dataframe
import pandas as pd
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)

# Créer 

with tab1 : 

  # Afficher le dataframe
  st.write(df_voitures)

with tab2 : 

  # Retravailler le dataframe
  df_voitures['continent'] = df_voitures['continent'].factorize()[0]

  # Réaliser une heatmap
  import seaborn as sns
  viz_correlation = sns.heatmap(df_voitures.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
  st.pyplot(viz_correlation.figure)

with tab3 : 

  st.write('nous allons réaliser une distribution')

# Réaliser une distribution


# %%writefile dataset_voitures.py
