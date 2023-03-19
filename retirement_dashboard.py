import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Load the data from the URL
url = 'https://data.drees.solidarites-sante.gouv.fr/explore/dataset/departretraite_parcsp/download?format=csv&timezone=Europe/Berlin&use_labels_for_header=false'
res = requests.get(url)
csv_file = res.content.decode('utf-8').splitlines()

# Load the data into a DataFrame
df = pd.read_csv(pd.io.common.StringIO('\n'.join(csv_file)), sep=';')

# Set the page title
st.set_page_config(page_title='Retirement Age and End-of-Career Conditions Dashboard', page_icon=':bar_chart:', layout='wide')

# Add a title to the dashboard
st.title('Retirement Age and End-of-Career Conditions by Socio-Professional Category')

# Add a section for selecting the category of socio-professional
cat_socp_list = df['cat_socp'].unique()
selected_cat_socp = st.sidebar.selectbox('Select a socio-professional category', cat_socp_list)

# Filter the DataFrame by the selected socio-professional category
filtered_df = df[df['cat_socp'] == selected_cat_socp]

# Display the filtered DataFrame
st.write(filtered_df)

# Create a histogram using Plotly Express
fig = px.histogram(filtered_df, x='age_median_depart', nbins=20, color='sexe', marginal='rug', barmode='overlay', title=f'Retirement Age Distribution for {selected_cat_socp}')
fig.update_layout(xaxis_title='Retirement Age', yaxis_title='Count')
st.plotly_chart(fig)

# Create a grouped bar chart using Plotly Express
fig2 = px.bar(filtered_df, x='cat_fin', y='pourc_salaries', color='sexe', title=f'End-of-Career Conditions for {selected_cat_socp}')
fig2.update_layout(xaxis_title='End-of-Career Conditions', yaxis_title='Percentage of Employees')
st.plotly_chart(fig2)
