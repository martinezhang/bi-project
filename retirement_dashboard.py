# Chargement des bibliothèques
import pandas as pd
import streamlit as st

# Chargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
data = pd.read_csv(url, sep=";")

# Nettoyage des données
data.iloc[:, 0] = data.iloc[:, 0].astype(int)  # conversion de la première colonne en entiers
data.dropna(inplace=True)  # suppression des lignes contenant des valeurs manquantes

# Liste des années et des catégories socioprofessionnelles
annees = sorted(data["annee"].unique())
categories = sorted(data["categorie_socioprofessionnelle"].unique())

# Création du dashboard
st.title("Age de départ à la retraite et conditions de fin de carrière selon la catégorie socioprofessionnelle")

# Filtres
selected_category = st.sidebar.selectbox("Sélectionnez une catégorie socioprofessionnelle", categories)
selected_year = st.sidebar.selectbox("Sélectionnez une année", annees)
selected_sex = st.sidebar.selectbox("Sélectionnez le sexe", ["Homme", "Femme"])
selected_region = st.sidebar.selectbox("Sélectionnez la région", sorted(data["region"].unique()))

# Filtrage des données selon les filtres sélectionnés
filtered_data = data[(data["categorie_socioprofessionnelle"] == selected_category) & (data["annee"] == selected_year) & (data["sexe"] == selected_sex) & (data["region"] == selected_region)]

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category, ", l'année", selected_year, ", le sexe", selected_sex, "et la région", selected_region)
st.write(filtered_data)

# Affichage de graphiques
st.subheader("Graphiques")
st.bar_chart(filtered_data[["age_conjoncturel_de_depart_a_la_retraite", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"]])
st.line_chart(filtered_data[["proportion_de_retraites_a_61_ans", "proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"]])
st.scatter_chart(filtered_data[["age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans"]])
