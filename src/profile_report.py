import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from lib import load, DataFrame, Graph


def group_data(df):
    df["datetime"] = pd.to_datetime(df["datetime"])
    df_grouped = (
        df.groupby(df["datetime"].dt.date)
        .agg(avg_temp=("temp", "mean"), avg_feel_like=("feelslike", "mean"))
        .reset_index()
    )
    return df_grouped


def generate_pdf(output_file, image_path, title="Graph Report"):
    # Create a PDF canvas
    c = canvas.Canvas(output_file, pagesize=letter)

    # Add a title
    c.setFont("Helvetica", 16)
    c.drawString(100, 750, title)

    # Insert the graph image into the PDF
    c.drawImage(image_path, 100, 400, width=400, height=300)

    # Save the PDF
    c.save()


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
    #
    # file_path = ""
    # try:
    #     file_path = "src/files"
    # except ModuleNotFoundError:
    file_path = "src/files"

    file_name = "Urban-Air-Quality-and-Health-Impact-Dataset.csv"
    dataframe = DataFrame(load(file_path, file_name))
    group_data = group_data(dataframe.get_df())
    graph = Graph(group_data, group_data["datetime"])
    prep_graph(graph, group_data)
    # graph.plot_and_save_graph()

    # Save the graph as an image
    graph_image_path = "output_graph.png"
    graph.plot_and_save_graph(save_path=graph_image_path)

    # Generate the PDF report with the saved graph
    generate_pdf(
        "output_report.pdf", graph_image_path, title="Temperature and Feels Like Report"
    )
