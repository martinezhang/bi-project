import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Load the data from the URL
url = 'https://www.data.gouv.fr/fr/datasets/r/83067d1a-a776-479f-9839-70e5ec5549a4'
res = requests.get(url)
csv_file = res.content.decode('utf-8').splitlines()

# Load the data into a DataFrame
df = pd.read_csv(pd.io.common.StringIO('\n'.join(csv_file)), sep=',')

# Set the page title
st.set_page_config(page_title='Retirement Age and End-of-Career Conditions Dashboard', page_icon=':bar_chart:', layout='wide')

# Add a title to the dashboard
st.title('Retirement Age and End-of-Career Conditions by Socio-Professional Category')

# Add a section for selecting the category of socio-professional
cat_socp_list = df['categorie_socioprofessionnelle'].unique()
selected_cat_socp = st.sidebar.selectbox('Select a socio-professional category', cat_socp_list)

# Filter the DataFrame by the selected socio-professional category
filtered_df = df[df['categorie_socioprofessionnelle'] == selected_cat_socp]

# Display the filtered DataFrame
st.write(filtered_df)

# Create a histogram using Plotly Express
fig = px.histogram(filtered_df, x='age_conjoncturel_de_depart_a_la_retraite', nbins=20, color='categorie_socioprofessionnelle',
                   marginal='rug', barmode='overlay', title=f'Retirement Age Distribution for {selected_cat_socp}')
fig.update_layout(xaxis_title='Retirement Age', yaxis_title='Count')
st.plotly_chart(fig)

# Create a grouped bar chart using Plotly Express
fig2 = px.bar(filtered_df, x='cat_fin', y='proportion_de_personnes_fortement_limitees_au_cours_de_la_premiere_annee_de_retraite', color='categorie_socioprofessionnelle',
               title=f'End-of-Career Conditions for {selected_cat_socp}')
fig2.update_layout(xaxis_title='End-of-Career Conditions', yaxis_title='Proportion of Retirees Strongly Limited During First Year of Retirement')
st.plotly_chart(fig2)

