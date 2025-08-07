
"""CSV Reader for creating a dashboard for data insights."""
import pandas as pd
import plotly.express as px
import streamlit as st

def plot_country_distribution(file_path):
    """Displays a pie chart of country distribution from the CSV."""
    # Load the CSV
    df = pd.read_csv(file_path)

    # Group by country and count occurrences
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']

    # Create pie chart
    fig = px.pie(
        country_counts,
        names='Country',
        values='Count',
        title='Distribution of People by Country'
    )

    # Show the chart
    fig.show()

st.set_page_config(page_title="Participant Data")

st.title("Alumni Data Insights")
st.write("Find out where our alumni are now.")

# File path to the CSV
CSV_FILE = 'participants.csv'

# Plot the distribution
plot_country_distribution(CSV_FILE)
