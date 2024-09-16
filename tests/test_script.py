import pytest
import pandas as pd
from io import StringIO
from src.lib import load, DataFrame, Graph
from src.profile_report import group_data, prep_graph

# Sample CSV data for testing
csv_data = """datetime,temp,feelslike
2024-09-07,98.5,95.9
2024-09-08,95.4,92.3
2024-09-09,94.7,90.6
2024-09-10,93.9,89.8
2024-09-11,94.0,90.0
"""


# Test for the group_data function
def test_group_data():
    df = pd.read_csv(StringIO(csv_data))
    grouped_df = group_data(df)

    assert "avg_temp" in grouped_df.columns
    assert "avg_feel_like" in grouped_df.columns
    assert grouped_df["avg_temp"].iloc[0] == 98.5
    assert grouped_df["avg_feel_like"].iloc[0] == 95.9


# Test for the prep_graph function
def test_prep_graph(mocker):
    df = pd.read_csv(StringIO(csv_data))
    grouped_df = group_data(df)

    # Create the Graph object
    graph = Graph(grouped_df, grouped_df["datetime"])

    # Prepare the graph for plotting
    prep_graph(graph, grouped_df)

    # Check that the dependent variables, title, and labels were set correctly
    assert len(graph.get_dependent_variables()) == 2
    assert graph.get_title() == "Average Temperature and Feels Like Over Time"
    assert graph.get_x_label() == "Date"
    assert graph.get_y_label() == "Values"