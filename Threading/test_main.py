import unittest
import threading
import queue
import time
import pandas as pd
from server import Server
from client import client_worker
from sqlite_db import SQLiteDB
from matplotlib_plot_manager import MatplotlibPlotManager

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_name = "aggi_data.db"
        cls.table_name = 'AGGI'
        cls.years = [str(year) for year in range(1979, 2023)]
        cls.columns = ['CO2', 'CH4', 'N2O', 'CFCs', 'HCFCs', 'HFCs']
        cls.result_queue = queue.Queue()

        # Start the server
        cls.server = Server('127.0.0.1', 65433, cls.db_name)
        cls.server_thread = threading.Thread(target=cls.server.start)
        cls.server_thread.start()
        time.sleep(1)  # Wait for the server to start

        # Initialize the SQLiteDB and create the table
        cls.db = SQLiteDB(cls.db_name)
        cls.db.connect()
        cls.db.create_table(cls.table_name, cls.columns)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_data_collection(self):
        threads = []
        for year in self.years:
            for column in self.columns:
                thread = threading.Thread(target=client_worker, args=(self.result_queue, year, column))
                threads.append(thread)
                thread.start()
                time.sleep(0.1)  # Slight delay to prevent server overload

        for thread in threads:
            thread.join()

        all_data = {}
        while not self.result_queue.empty():
            result = self.result_queue.get()
            year = list(result.keys())[0]
            if year not in all_data:
                all_data[year] = {}
            all_data[year].update(result[year])

        data = []
        for year in self.years:
            row = {"Year": year}
            row.update(all_data.get(year, {}))
            data.append(row)

        df = pd.DataFrame(data)
        self.assertFalse(df.empty, "DataFrame is empty. Data collection failed.")

        for column in self.columns:
            self.assertIn(column, df.columns, f"{column} is not in the DataFrame columns.")

        # Plotting test (visual inspection required)
        plot_manager = MatplotlibPlotManager(df)
        for gas in self.columns:
            plot_manager.plot_regression('Year', gas, title=f'Linear Regression of {gas} over Years')

if __name__ == "__main__":
    unittest.main()
