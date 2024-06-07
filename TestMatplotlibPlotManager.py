import unittest
import pandas as pd
from matplotlib import pyplot as plt
from MatplotlibPlotManagerClass import MatplotlibPlotManager

class TestMatplotlibPlotManager(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [2, 3, 5, 7, 11],
            'z': [1, 4, 9, 16, 25]
        })
        self.plot_manager = MatplotlibPlotManager(self.data)
    
    def test_initialization(self):
        self.assertEqual(self.plot_manager.data.equals(self.data), True)
    
    def test_dunder_str(self):
        expected_str = "PlotManager handling DataFrame with 5 rows and 3 columns."
        self.assertEqual(str(self.plot_manager), expected_str)
    
    def test_dunder_repr(self):
        expected_repr = f"PlotManager(data={self.data})"
        self.assertEqual(repr(self.plot_manager), expected_repr)
    
    def test_dunder_getitem(self):
        self.assertTrue(self.plot_manager['x'].equals(self.data['x']))
        self.assertTrue(self.plot_manager['y'].equals(self.data['y']))
        self.assertTrue(self.plot_manager['z'].equals(self.data['z']))
    
    def test_plot_line(self):
        self.plot_manager.plot_line('x', 'y', title="Test Line Plot")
        plt.close()

    def test_plot_bar(self):
        self.plot_manager.plot_bar('x', 'y', title="Test Bar Plot")
        plt.close()

    def test_plot_scatter(self):
        self.plot_manager.plot_scatter('x', 'y', title="Test Scatter Plot")
        plt.close()

    def test_plot_histogram(self):
        self.plot_manager.plot_histogram('y', bins=5, title="Test Histogram")
        plt.close()

if __name__ == '__main__':
    unittest.main()
