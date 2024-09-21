import pytest
import polars as pl
from io import StringIO
from src.lib import DataFrame, Graph

csv_data = """datetime,temp,feelslike
2024-09-07,98.5,95.9
2024-09-08,95.4,92.3
2024-09-09,94.7,90.6
2024-09-10,93.9,89.8
2024-09-11,94.0,90.0
"""


def test_dataframe_mean():
    df = pl.read_csv(StringIO(csv_data))
    df_class = DataFrame()
    df_class.set_df(df)
    assert df_class.get_mean("temp") == pytest.approx(95.3, 0.1)


def test_dataframe_median():
    df = pl.read_csv(StringIO(csv_data))
    df_class = DataFrame()
    df_class.set_df(df)
    assert df_class.get_median("temp") == pytest.approx(94.7, 0.1)


def test_dataframe_sd():
    df = pl.read_csv(StringIO(csv_data))
    df_class = DataFrame()
    df_class.set_df(df)
    assert df_class.get_sd("temp") == pytest.approx(1.7638, 0.1)

