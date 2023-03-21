import pandas as pd
import plotly.express as px

# Charger les données
data = pd.read_csv("donnees_retraite.csv")

# Créer le dashboard
dashboard = px.scatter(data, x="annee", y="proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite",
                        color="categorie_socioprofessionnelle",
                        hover_data=["proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite",
                                    "age_conjoncturel_de_depart_a_la_retraite", "proportion_de_retraites_a_61_ans",
                                    "duree_moyenne_en_emploi_hors_cumul", "duree_moyenne_sans_emploi_ni_retraite"])

# Appliquer les filtres
dashboard.update_traces(visible="legendonly", selector=dict(name="proportion_de_personnes_limitees_mais_pas_fortement_au_cours_de_la_premiere_annee_de_retraite"))
dashboard.update_traces(visible="legendonly", selector=dict(name="age_conjoncturel_de_depart_a_la_retraite"))
dashboard.update_traces(visible="legendonly", selector=dict(name="proportion_de_retraites_a_61_ans"))
dashboard.update_traces(visible="legendonly", selector=dict(name="duree_moyenne_en_emploi_hors_cumul"))
dashboard.update_traces(visible="legendonly", selector=dict(name="duree_moyenne_sans_emploi_ni_retraite"))

# Afficher le dashboard
dashboard.show()
