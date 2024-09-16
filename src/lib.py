import matplotlib.pyplot as plt
import pandas as pd


def load(file_path, file_name):
    return pd.read_csv(file_path + "/" + file_name)


class DataFrame:
    def __init__(self, df=None):
        self.df = df

    def set_df(self, df):
        self.df = df

    def get_df(self):
        return self.df

    def get_mean(self, column_name):
        return self.df[column_name].mean()

    def get_median(self, column_name):
        return self.df[column_name].median()

    def get_sd(self, column_name):
        return self.df[column_name].std()


class Graph:
    def __init__(self, df, independent_variable):
        self.independent_variables = independent_variable
        self.df = df
        self.dependent_variables = []
        self.title = ""
        self.x_label = ""
        self.y_label = ""

    def set_df(self, df):
        self.df = df

    def set_independent_variables(self, independent_variables):
        self.independent_variables = independent_variables

    def set_dependent_variables(self, dependent_variables):
        self.dependent_variables = dependent_variables

    def set_title(self, title):
        self.title = title

    def set_x_label(self, x_label):
        self.x_label = x_label

    def set_y_label(self, y_label):
        self.y_label = y_label

    def get_df(self):
        return self.df

    def get_dependent_variables(self):
        return self.dependent_variables

    def get_independent_variables(self):
        return self.independent_variables

    def get_title(self):
        return self.title

    def get_x_label(self):
        return self.x_label

    def get_y_label(self):
        return self.y_label

    def plot_y_axis(self, dependent_variable):
        plt.plot(
            self.get_independent_variables(),
            dependent_variable["data"],
            label=dependent_variable["label"],
            color=dependent_variable["co"],
            marker="o",
        )

    def report_statistics(self, dependent_variable):
        data = dependent_variable["data"]
        mean = round(data.mean(), 2)
        median = round(data.median(), 2)
        std_dev = round(data.std(), 2)
        print(
            f'{dependent_variable["label"]} - '
            f"Mean: {mean}, "
            f"Median: {median}, "
            f"Std Dev: {std_dev}"
        )

    def plot_and_show_graph(self):
        for dependent_variable in self.get_dependent_variables():
            self.report_statistics(dependent_variable)
            self.plot_y_axis(dependent_variable)
        plt.title = self.get_title()
        plt.xlabel = self.get_x_label()
        plt.ylabel = self.get_y_label()
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
