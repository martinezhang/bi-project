import pandas as pd
import streamlit as st

# Chargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
data = pd.read_csv(url, sep=";")

# Création du dashboard
st.title("Age de départ à la retraite et conditions de fin de carrière selon la catégorie socioprofessionnelle")
categories = data["categorie_socioprofessionnelle"].unique()
selected_category = st.sidebar.selectbox("Sélectionnez une catégorie socioprofessionnelle", categories)

# Filtre les données selon la catégorie sélectionnée
filtered_data = data[(data["categorie_socioprofessionnelle"] == selected_category) & (data[annee] == selected_year)]

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category)
st.write(filtered_data)

# Affichage de graphiques
st.subheader("Graphiques")
st.bar_chart(filtered_data[["age_conjoncturel_de_depart_a_la_retraite", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"]])
st.line_chart(filtered_data[["proportion_de_retraites_a_61_ans", "proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"]])
