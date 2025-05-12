import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('owid-covid-data.csv')

# Sidebar for user input
st.sidebar.title("COVID-19 Dashboard")
countries = df['location'].unique()
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=['United States', 'India', 'Brazil'])

# Filter data based on selection
df_filtered = df[df['location'].isin(selected_countries)]

# Title of the dashboard
st.title("COVID-19 Data Dashboard")

# Total cases over time
st.subheader("Total Cases Over Time")
fig_cases = px.line(df_filtered, x='date', y='total_cases', color='location', title='Total COVID-19 Cases Over Time')
st.plotly_chart(fig_cases)

# Total deaths over time
st.subheader("Total Deaths Over Time")
fig_deaths = px.line(df_filtered, x='date', y='total_deaths', color='location', title='Total COVID-19 Deaths Over Time')
st.plotly_chart(fig_deaths)

# New cases over time
st.subheader("Daily New Cases")
fig_new_cases = px.line(df_filtered, x='date', y='new_cases', color='location', title='Daily New COVID-19 Cases')
st.plotly_chart(fig_new_cases)

# Vaccination progress
st.subheader("Vaccination Progress Over Time")
fig_vaccinations = px.line(df_filtered, x='date', y='total_vaccinations', color='location', title='Total COVID-19 Vaccinations Over Time')
st.plotly_chart(fig_vaccinations)

# Insights section
st.subheader("Key Insights")
st.write("""
- The dashboard allows for interactive exploration of COVID-19 data across selected countries.
- Users can visualize trends in total cases, deaths, new cases, and vaccination progress.
- Insights can be drawn based on the visualizations to understand the pandemic's impact better.
""")