import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy

# Présentation quête
st.title(':blue[Quête] : Streamlit : build and share data apps &mdash;\
            :chart_with_upwards_trend:')

st.markdown("""
- Une analyse de corrélation et de distribution grâce à **différents graphiques et des commentaires**.
- **Des boutons** doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
- L'application doit être **disponible** sur la plateforme de partage.
""")

df_voiture = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# Sélecteur de bouton
# Pour mettre le sélecteur sur le côté : st.sidebar.selectbox("Sélectionnez le pays", ("US", "Europe", "Japon"))
selecte_country = st.selectbox("Sélectionnez le pays", ("US.", "Europe.", "Japan."))
#st.write(selecte_country)
#st.dataframe(df_voiture[df_voiture['continent'].str.contains('US.')])

if selecte_country:
    df_voiture_filtre = df_voiture[df_voiture['continent'].str.contains(selecte_country)]

    # Partie analyse

    st.header('1. Analyse', divider='rainbow')

    #Affichage du dataframe
    st.write("Dataframe voiture")
    st.write(df_voiture_filtre)


    #Graphique heatmap
    viz_heatmap = sns.heatmap(df_voiture_filtre.select_dtypes(include = ['int', 'float']).corr(), cmap = 'coolwarm')
    plt.title('Correlation Heatmap Voiture')
    st.pyplot(viz_heatmap.figure)

    # Graphique pairplot
    st.subheader("Pair plot voiture")
    pair_plot = px.scatter_matrix(df_voiture_filtre, dimensions=["mpg", "cylinders", "cubicinches", "hp", "weightlbs", "time-to-60"], color='continent')
    st.plotly_chart(pair_plot)


    # Graphique histogramme

    st.subheader("Histogramme weightlbs")
    histogram_weightlbs = px.histogram(df_voiture_filtre, x="weightlbs")
    st.plotly_chart(histogram_weightlbs)

    st.subheader("Histogramme hp")
    histogram_hp = px.histogram(df_voiture_filtre, x="hp")
    st.plotly_chart(histogram_hp)

    st.subheader("Histogramme time to 60")
    histogram_hp = px.histogram(df_voiture_filtre, x="time-to-60")
    st.plotly_chart(histogram_hp)

# Partie commentaires 

st.header('2. Commmentaires &mdash;\
            :chart_with_upwards_trend: - :flag-fr: - :flag-us: - :jp:', divider='rainbow')

st.markdown("""
- Grâce au pair plot et à la heatmap, on constate une **corrélation positive** entre 4 variables :"mpg", "cylinders", "cubicinches", "hp".
- La :blue[**France**] a des véhicules plus légers (que US et Japan), le puissance est globalement entre US et Japon, et le time to 60 et légerement plus éléve que les US.
- Les :blue[**US**] ont des chiffres globalement plus élévés : Les véhicules ont plus de puissance, plus lourds mais le time to 60 est plus faible que les japonais  .
- Les :blue[**Japonais**] ont des véhicules plus lourds, avec une puissance pas forcément très élévée, et donc augmente le time to 60 
""")