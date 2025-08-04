
"""CSV Reader for creating a dashboard for data insights."""

import csv
import pandas as pd
import plotly.express as px

def organise_participant_data():
    """Reads participant data CSV and returns formatted strings"""
    participants = []

    with open('participants.csv', 'r', encoding="utf-8") as file:
        participant_data = csv.reader(file)

    for row in participant_data:
        participant_id = row[0]
        first_name = row[2]
        last_name = row[3]
        email = row[9]
        participants.append(
            f"Customer #{participant_id}, {first_name} {last_name}, {email}")

    return participants

def display_participant():
    """Displays participant data"""
    for participant in organise_participant_data():
        print(participant)

display_participant()
