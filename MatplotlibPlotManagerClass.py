import pandas as pd
import matplotlib.pyplot as plt

class MatplotlibPlotManager:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def __str__(self):
        return f"PlotManager handling DataFrame with {self.data.shape[0]} rows and {self.data.shape[1]} columns."

    def __repr__(self):
        return f"PlotManager(data={self.data})"

    def __getitem__(self, item):
        return self.data[item]

    def _set_plot_details(self, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def plot_line(self, x_col: str, y_col: str, title: str = "Line Plot", xlabel: str = "", ylabel: str = ""):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data[x_col], self.data[y_col])
        self._set_plot_details(title, xlabel if xlabel else x_col, ylabel if ylabel else y_col)
        plt.show()

    def plot_bar(self, x_col: str, y_col: str, title: str = "Bar Plot", xlabel: str = "", ylabel: str = ""):
        plt.figure(figsize=(10, 6))
        plt.bar(self.data[x_col], self.data[y_col])
        self._set_plot_details(title, xlabel if xlabel else x_col, ylabel if ylabel else y_col)
        plt.show()

    def plot_scatter(self, x_col: str, y_col: str, title: str = "Scatter Plot", xlabel: str = "", ylabel: str = ""):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[x_col], self.data[y_col])
        self._set_plot_details(title, xlabel if xlabel else x_col, ylabel if ylabel else y_col)
        plt.show()

    def plot_histogram(self, col: str, bins: int = 10, title: str = "Histogram", xlabel: str = "", ylabel: str = "Frequency"):
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[col], bins=bins)
        self._set_plot_details(title, xlabel if xlabel else col, ylabel)
        plt.show()
