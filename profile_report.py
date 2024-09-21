
import polars as pl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from src.lib import load_with_polar, DataFrame, Graph


def group_data(df):
    df = df.with_columns(pl.col("datetime").str.to_datetime("%Y-%m-%d"))
    return df.group_by(df["datetime"]).agg(
        avg_temp=pl.col("temp").mean(),
        avg_feel_like=pl.col("feelslike").mean()).sort("datetime")


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

    file_path = "src/files"
    file_name = "Urban-Air-Quality-and-Health-Impact-Dataset.csv"
    dataframe = DataFrame(load_with_polar(file_path, file_name))
    group_data = group_data(dataframe.get_df())
    graph = Graph(group_data, group_data["datetime"])
    prep_graph(graph, group_data)
    graph_image_path = "./output_graph.png"
    graph.plot_and_save_graph(save_path=graph_image_path)

    generate_pdf(
        "./output_report.pdf", graph_image_path, title="Temperature and Feels Like Report"
    )

