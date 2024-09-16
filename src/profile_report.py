import pandas as pd
from src.lib import load, DataFrame, Graph


def group_data(df):
    df["datetime"] = pd.to_datetime(df["datetime"])
    df_grouped = (
        df.groupby(df["datetime"].dt.date)
        .agg(avg_temp=("temp", "mean"), avg_feel_like=("feelslike", "mean"))
        .reset_index()
    )
    return df_grouped


def prep_graph(g, g_df):
    g.set_dependent_variables(
        [
            {"data": g_df["avg_temp"], "label": "Temp", "co": "r"},
            {"data": g_df["avg_feel_like"], "label": "Feels", "co": "b"},
        ]
    )
    g.set_title("Average Temperature and Feels Like Over Time")
    g.set_x_label("Date")
    g.set_y_label("Values")


if __name__ == "__main__":
    file_path = "./files"
    file_name = "Urban-Air-Quality and-Health-Impact-Dataset.csv"
    dataframe = DataFrame(load(file_path, file_name))
    group_data = group_data(dataframe.get_df())
    graph = Graph(group_data, group_data["datetime"])
    prep_graph(graph, group_data)
    graph.plot_and_show_graph()
