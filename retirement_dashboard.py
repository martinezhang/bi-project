import pandas as pd
import streamlit as st
import plotly.express as px

# Chargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
data = pd.read_csv(url, sep=";")

# Nettoyage des données
data.iloc[:, 0] = data.iloc[:, 0].astype(int)  # conversion de la première colonne en entiers
data.dropna(inplace=True)  # suppression des lignes contenant des valeurs manquantes

# Liste des années
annees = sorted(data["annee"].unique())

# Création du dashboard
st.title("Age de départ à la retraite et conditions de fin de carrière selon la catégorie socioprofessionnelle")

# Filtres
selected_category = st.sidebar.selectbox("Sélectionnez une catégorie socioprofessionnelle", sorted(data["categorie_socioprofessionnelle"].unique()))
selected_year = st.sidebar.selectbox("Sélectionnez une année", annees)
selected_region = st.sidebar.selectbox("Sélectionnez une région", sorted(data["region"].unique()))

# Filtrage des données selon les filtres sélectionnés
filtered_data = data[(data["categorie_socioprofessionnelle"] == selected_category) & (data["annee"] == selected_year) & (data["region"] == selected_region)]

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category, "l'année", selected
