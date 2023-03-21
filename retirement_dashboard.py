import pandas as pd
import streamlit as st

# Chargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"
df = pd.read_csv(url, sep=";")

# Renommer les colonnes
df = df.rename(columns={
    "proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite": "fortement_limite",
    "proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite": "limite",
    "age_conjoncturel_de_depart_a_la_retraite": "age_depart",
    "proportion_de_retraites_a_61_ans": "retraite_61",
    "duree_moyenne_en_emploi_hors_cumul": "duree_emploi",
    "duree_moyenne_sans_emploi_ni_retraite": "duree_chomage"
})

# Supprimer les colonnes inutiles
df = df.drop(["mois", "sexe"], axis=1)

# Convertir la colonne annee en type datetime
df["annee"] = pd.to_datetime(df["annee"], format="%Y")

# Créer le tableau de bord avec Streamlit
st.title("Tableau de bord de la base de données des retraites")
st.dataframe(df)
