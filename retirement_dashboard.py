import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Remplacez cette URL par l'URL de votre fichier CSV
URL_CSV = "https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4"

# Téléchargez le fichier CSV
response = requests.get(URL_CSV)
csv_content = StringIO(response.text)

# Chargez le fichier CSV dans un DataFrame Pandas
data = pd.read_csv(csv_content)

# Affichez le contenu du fichier CSV sur Streamlit
st.title("Visualisation des données CSV")
st.write(data)
