import pandas as pd
import streamlit as st
import altair as alt

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
#selected_min_proportion_fortement_limitees = st.sidebar.slider("Sélectionnez la proportion minimale de personnes fortement limitées au cours de la première année de retraite", 0, 100, 0, 5)
#selected_max_proportion_fortement_limitees = st.sidebar.slider("Sélectionnez la proportion maximale de personnes fortement limitées au cours de la première année de retraite", 0, 100, 100, 5)
#selected_min_proportion_limitees_mais_pas_fortement = st.sidebar.slider("Sélectionnez la proportion minimale de personnes limitées mais pas fortement au cours de la première année de retraite", 0, 100, 0, 5)
#selected_max_proportion_limitees_mais_pas_fortement = st.sidebar.slider("Sélectionnez la proportion maximale de personnes limitées mais pas fortement au cours de la première année de retraite", 0, 100, 100, 5)
selected_age_conjoncturel = st.sidebar.multiselect("Sélectionnez les tranches d'âge pour l'âge conjoncturel de départ à la retraite", sorted(data["age_conjoncturel_de_depart_a_la_retraite"].unique()))
selected_min_proportion_retraites = st.sidebar.slider("Sélectionnez la proportion minimale de retraités à 61 ans", 0, 100, 0, 5)
selected_max_proportion_retraites = st.sidebar.slider("Sélectionnez la proportion maximale de retraités à 61 ans", 0, 100, 100, 5)
selected_duree_moyenne_en_emploi_hors_cumul = st.sidebar.multiselect("Sélectionnez les tranches de durée pour la durée moyenne en emploi hors cumul", sorted(data["duree_moyenne_en_emploi_hors_cumul"].unique()))
selected_duree_moyenne_sans_emploi_ni_retraite = st.sidebar.multiselect("Sélectionnez les tranches de durée pour la durée moyenne sans emploi ni retraite", sorted(data["duree_moyenne_sans_emploi_ni_retraite"].unique()))

# Filtrage des données selon les filtres sélectionnés
filtered_data = data[(data["categorie_socioprofessionnelle"] == selected_category) & (data["annee"] == selected_year)]
#filtered_data = filtered_data[(filtered_data["proportion_fortement_limitees"] >= selected_min_proportion_fortement_limitees/100) & (filtered_data["proportion_fortement_limitees"] <= selected_max_proportion_fortement_limitees/100)]
#filtered_data = filtered_data[(filtered_data["proportion_limitees_mais_pas_fortement"] >= selected_min_proportion_limitees_mais_pas_fortement/100) & (filtered_data["proportion_limitees_mais_pas_fortement"] <= selected_max_proportion_limitees_mais_pas_fortement/100)]
filtered_data = filtered_data[filtered_data["age_conjoncturel_de_depart_a_la_retraite"].isin(selected_age_conjoncturel)]
filtered_data = filtered_data[(filtered_data["proportion_retraites_a_61_ans"] >= selected_min_proportion_retraites/100) & (filtered_data["proportion_retraites_a_61_ans"] <= selected_max_proportion_retraites/100)]
filtered_data = filtered_data[filtered_data["duree_moyenne_en_emploi_hors_cumul"].isin(selected_duree_moyenne_en_emploi_hors_cumul)]
filtered_data = filtered_data[filtered_data["duree_moyenne_sans_emploi_ni_retraite"].isin(selected_duree_moyenne_sans_emploi_ni_retraite)]

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category, "et l'année", selected_year)
st.write(filtered_data)

# Affichage de graphiques
st.subheader("Graphiques")
st.bar_chart(filtered_data[["age_conjoncturel_de_depart_a_la_retraite", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"]])
st.line_chart(filtered_data[["proportion_de_retraites_a_61_ans", "proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"]]) 

