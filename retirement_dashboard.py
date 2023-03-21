import pandas as pd
import streamlit as st

# Chargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
data = pd.read_csv(url, sep=";")

# Transformer la première colonne en entiers et prendre toutes les valeurs de la colonne comme années
data.iloc[:, 0] = data.iloc[:, 0].astype(int)
annees = data.iloc[:, 0].astype(int).unique()

# Création du dashboard
st.title("Age de départ à la retraite et conditions de fin de carrière selon la catégorie socioprofessionnelle")
categories = sorted(data["categorie_socioprofessionnelle"].unique())
selected_category = st.sidebar.selectbox("Sélectionnez une catégorie socioprofessionnelle", categories)

# Filtre les données selon la catégorie sélectionnée
filtered_data = data[data["categorie_socioprofessionnelle"] == selected_category]

# Filtrer les données selon l'année sélectionnée
selected_year = st.sidebar.selectbox("Sélectionnez une année", annees)
filtered_data = filtered_data[filtered_data["annee"] == selected_year]

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category, "et l'année", selected_year)
st.write(filtered_data)
