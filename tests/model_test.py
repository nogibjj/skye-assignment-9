import pytest


def test_notebook():
    pytest.main(["--nbval", "./model.ipynb"])
