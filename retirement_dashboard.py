import streamlit as st
import pandas as pd

url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
data = pd.read_csv(url, sep=";")

# Sidebar pour filtrer les données
year = st.sidebar.slider("Année", min_value=data["annee"].min(), max_value=data["annee"].max())
category = st.sidebar.selectbox("Catégorie socioprofessionnelle", data["categorie_socioprofessionnelle"].unique())

# Filtrer les données
filtered_data = data[(data["annee"] == year) & (data["categorie_socioprofessionnelle"] == category)]

# Afficher les données filtrées
st.write("Données pour l'année", year, "et la catégorie", category)
st.write(filtered_data)

# Créer des graphiques à partir des données filtrées
st.write("Proportion de personnes limitées au cours de la première année de retraite")
st.bar_chart(filtered_data[["proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"]])

st.write("Âge conjoncturel de départ à la retraite")
st.line_chart(filtered_data["age_conjoncturel_de_depart_a_la_retraite"])

st.write("Proportion de retraités à 61 ans")
st.area_chart(filtered_data["proportion_de_retraites_a_61_ans"])

st.write("Durée moyenne en emploi hors cumul")
st.line_chart(filtered_data["duree_moyenne_en_emploi_hors_cumul"])

st.write("Durée moyenne sans emploi ni retraite")
st.line_chart(filtered_data["duree_moyenne_sans_emploi_ni_retraite"])

st.write("Durée moyenne en emploi hors cumul par catégorie socioprofessionnelle")
mean_duration_by_category = data.groupby("categorie_socioprofessionnelle")["duree_moyenne_en_emploi_hors_cumul"].mean()
st.bar_chart(mean_duration_by_category)

st.write("Âge conjoncturel de départ à la retraite par catégorie socioprofessionnelle")
mean_age_by_category = data.groupby("categorie_socioprofessionnelle")["age_conjoncturel_de_depart_a_la_retraite"].mean()
st.bar_chart(mean_age_by_category)
