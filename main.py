
"""CSV Reader for creating a dashboard for data insights."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def plot_country_distribution(file_path):
    """Displays a pie chart of country distribution from the CSV."""
    # Load the CSV
    df = pd.read_csv(file_path)
    # Group by country and count occurrences
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    # Count how many unique countries there are
    num_countries = country_counts.shape[0]
    # Add text before the chart
    st.write(f"In 2024, we had participants from **{num_countries} countries** on our programmes.")
    # Create pie chart
    fig = px.pie(
        country_counts,
        names='Country',
        values='Count',
        title='Participants by Nationality'
    )
    # Show the chart
    st.plotly_chart(fig)
def plot_ethnicity_distribution(file_path):
    """Displays a pie chart of ethnicity distribution from the CSV."""
    # Load the CSV
    df = pd.read_csv(file_path)
    # --- Calculation for BIPOC percentage ---
    non_white_participants = df[df['Ethnicity'] != "White"]
    # Count the number of non-White participants
    num_bipoc = non_white_participants.shape[0]
    # Calculate the total number of participants
    total_participants = df.shape[0]
    # Calculate the percentage of BIPOC participants
    percentage_bipoc = (num_bipoc / total_participants) * 100
    # Add text before the chart
    st.write(
        f"**{int(percentage_bipoc)}%** of these participants were"
        " from Black, Asian or ethnic minority backgrounds." 
    )
    # --- Pie chart for ethnicity distribution ---
    # Group by ethnicity and count occurrences
    ethnicity_counts = df['Ethnicity'].value_counts().reset_index()
    ethnicity_counts.columns = ['Ethnicity', 'Count']
    # Create pie chart
    fig = px.pie(
        ethnicity_counts,
        names='Ethnicity',
        values='Count',
        title='Participants by Ethnicity'
    )
    # Show the chart
    st.plotly_chart(fig)
def plot_confidence_by_school(file_path):
    """Displays a grouped bar chart of confidence growth from the CSV."""
    # Load the CSV
    df = pd.read_csv(file_path)
    # Group and count responses per school and confidence level
    counts = df.groupby(['School', 'Confidence']).size().reset_index(name='Count')
    # Definition of increased confidence
    increased_confidence = ["More confident", "Much more confident"]
    # Count how many participants reported increased confidence
    num_increased = df[df["Confidence"].isin(increased_confidence)].shape[0]
    # Calculate the total number of participants
    total_participants = df.shape[0]
    # Calculate the percentage
    percentage_increased = (num_increased / total_participants) * 100
    # Add text before the chart
    st.write(
        f"In 2024, **{int(percentage_increased)}%** of participants"
        " felt they had increased in confidence."
    )
    # Create a grouped bar chart
    fig = px.bar(
        counts,
        x='School',
        y='Count',
        color='Confidence',
        barmode='group',
        title='Confidence Levels After Completing Our Programme (by School)'
    )

    st.plotly_chart(fig)
def plot_skills_development(file_path):
    """Displays a bar charts of skills growth from the CSV."""
    # Load the CSV
    df = pd.read_csv(file_path)
    # Calculate average "before" and "after" scores for each skill area
    def scale_to_percent(series):
        return round(series.mean() / 5 * 100, 1)  # scale from 1–5 to percentage

    data = {
        "Skill Area": [
            "Career Awareness", 
            "Presentation Skills", 
            "Interview Skills", 
            "CV Development"
        ],
        "Before": [
            scale_to_percent(df["Career Awareness Before"]),
            scale_to_percent(df["Presentation Before"]),
            scale_to_percent(df["Interview Before"]),
            scale_to_percent(df["CV Development Before"])
        ],
        "After": [
            scale_to_percent(df["Career Awareness After"]),
            scale_to_percent(df["Presentation After"]),
            scale_to_percent(df["Interview After"]),
            scale_to_percent(df["CV Development After"])
        ]
    }

    # Convert to DataFrame for clarity
    results_df = pd.DataFrame(data)
    results_df["Increase"] = results_df["After"] - results_df["Before"]

    #
    st.write(
        "We're thrilled to see the percentage increases in all the skills we measure " 
        "following our Future Skills and Employability Skills pathways." 
    )

    # Create Plotly bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=results_df["Skill Area"],
        y=results_df["Before"],
        name='Before',
        marker_color='lightslategray'
    ))

    fig.add_trace(go.Bar(
        x=results_df["Skill Area"],
        y=results_df["After"],
        name='After',
        marker_color='seagreen'
    ))

    # Annotate percentage increase on top
    for _, row in results_df.iterrows():
        fig.add_annotation(
            x=row["Skill Area"],
            y=row["After"] + 3,
            text=f"+{row['Increase']:.0f}%",
            showarrow=False,
            font=dict(size=12, color="black")
        )

    # Layout
    fig.update_layout(
        title="Skill Self Assessments (Meaured Before vs After Our Programme)",
        yaxis_title="Average Rating (%)",
        barmode='group',
        yaxis=dict(range=[0, 110])
    )

    # Streamlit display percentages
    st.plotly_chart(fig)
st.set_page_config(page_title="Participant Data Impact Report")

st.title("Participant Data Impact Report")
st.write(
    "We've heard directly from young people, employers and supporters about the "
    "impact our work has had on them, as we "
    "look back on a decade of transforming young people's lives, and commit to "
    "making even more of an impact in our programmes across the next year and beyond."
)

# File path to the CSV
CSV_FILE = 'participants.csv'

st.markdown("### Diversity of Participants")

# Plot nationality pie chart
plot_country_distribution(CSV_FILE)

st.write(
        "All participants in our programmes are recipients "
        "of free school meals."
    )

# Plot ethnicity pie chart
plot_ethnicity_distribution(CSV_FILE)

st.markdown("### Skills Development")
st.write(
    "We survey our participants at the beginning and end of every" 
    " employability, skills and work experience programme." 
)

# Plot the confidence growth by school
plot_confidence_by_school(CSV_FILE)

# Plot the skills growth percentages
plot_skills_development(CSV_FILE)

st.markdown("### Alumni Data Insights")
st.write(
    "Find out where our alumni are now. Five years after completing our programme," 
    " we're thrilled to see what our alumni have achieved."
)
