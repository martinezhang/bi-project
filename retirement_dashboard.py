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

# Créer un graphique avec une ligne par catégorie socioprofessionnelle pour chaque année
graph_data = filtered_data.groupby(['annee', 'categorie_socioprofessionnelle']).mean().reset_index()
chart = st.line_chart(graph_data, use_container_width=True, height=500)

# Ajouter une ligne de couleur différente pour chaque catégorie socioprofessionnelle
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
color_map = {category: color for category, color in zip(categories, colors)}
for i, line in enumerate(chart.chart_data['data']):
    category = line['name'].split('=')[1]
    color = color_map[category]
    chart.chart_data['data'][i]['line']['color'] = color

# Affichage des données
st.write("Données pour la catégorie socioprofessionnelle :", selected_category, "et l'année", selected_year)
st.write(filtered_data)

# Affichage de graphiques
st.subheader("Graphiques")
st.bar_chart(filtered_data[["age_conjoncturel_de_depart_a_la_retraite", "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"]])
st.line_chart(graph_data[["annee", "proportion_de_retraites_a_61_ans", "proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite", "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"]]) 
