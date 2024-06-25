import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

    def plot_regression(self, x_col: str, y_col: str, title: str = "Linear Regression", xlabel: str = "", ylabel: str = ""):
        plt.figure(figsize=(10, 6))
        x = self.data[x_col].astype(float)
        y = self.data[y_col].astype(float)
        plt.scatter(x, y, label='Data Points')
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), "r--", label='Regression Line')
        self._set_plot_details(title, xlabel if xlabel else x_col, ylabel if ylabel else y_col)
        plt.legend()
        plt.show()

    def plot_all_regressions(self, x_col: str):
        for y_col in self.data.columns:
            if y_col != x_col:
                self.plot_regression(x_col, y_col, title=f'Linear Regression of {y_col} over {x_col}')

if __name__ == "__main__":
    # Example usage
    data = {
        'Year': [1979, 1980, 1981, 1982, 1983],
        'CO2': [1.025, 1.035, 1.045, 1.055, 1.065],
        'CH4': [0.500, 0.510, 0.520, 0.530, 0.540],
        'N2O': [0.088, 0.090, 0.092, 0.094, 0.096],
        'CFCs': [0.175, 0.180, 0.185, 0.190, 0.195],
        'HCFCs': [0.008, 0.009, 0.010, 0.011, 0.012],
        'HFCs': [0.001, 0.002, 0.003, 0.004, 0.005],
    }
    df = pd.DataFrame(data)
    plot_manager = MatplotlibPlotManager(df)
    plot_manager.plot_all_regressions('Year')
