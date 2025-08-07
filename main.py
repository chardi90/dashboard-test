
"""CSV Reader for creating a dashboard for data insights."""
import pandas as pd
import plotly.express as px

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

# File path to the CSV
CSV_FILE = 'participants.csv'

# Plot the distribution
plot_country_distribution(CSV_FILE)
