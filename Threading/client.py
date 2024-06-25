import socket
import json
import threading
import queue
import time
import pandas as pd
from ByteStreamClass import StringConverter
from matplotlib_plot_manager import MatplotlibPlotManager

class Client:
    def __init__(self, host: str, port: int, result_queue, year, column):
        self.host = host
        self.port = port
        self.client_socket = None
        self.converter = StringConverter()
        self.result_queue = result_queue
        self.year = year
        self.column = column
        self.connect()

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
        except Exception as e:
            print(f"Connection error: {e}")
            self.client_socket = None

    def send_request(self, query: str):
        try:
            self.converter.set_input_string(query)
            self.converter.send_byte_stream(self.client_socket)
            response = self.converter.receive_byte_stream(self.client_socket)
            return response
        except Exception as e:
            print(f"Error sending request: {e}")
            return None

    def fetch_data(self):
        query = json.dumps({"year": self.year, "column": self.column})
        response = self.send_request(query)
        if response:
            try:
                self.result_queue.put(json.loads(response))
            except json.JSONDecodeError:
                print(f"Failed to decode JSON response for {self.year}, {self.column}: {response}")
        else:
            print(f"Failed to fetch data for {self.year}, {self.column}")

    def close(self):
        if self.client_socket:
            self.client_socket.close()

def client_worker(result_queue, year, column):
    client = Client('127.0.0.1', 65433, result_queue, year, column)
    if client.client_socket:
        client.fetch_data()
        client.close()
    else:
        print(f"Client failed to connect for {year}, {column}")

if __name__ == "__main__":
    result_queue = queue.Queue()
    years = [str(year) for year in range(1979, 2023)]
    columns = ['CO_2', 'CH_4', 'N_2_O', 'CFCs', 'HCFCs', 'HFCs']

    threads = []
    for year in years:
        for column in columns:
            thread = threading.Thread(target=client_worker, args=(result_queue, year, column))
            threads.append(thread)
            thread.start()
            time.sleep(0.1)  # Slight delay to prevent server overload

    for thread in threads:
        thread.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    # Process results into DataFrame
    data_dict = {year: {col: None for col in columns} for year in years}
    for result in results:
        if isinstance(result, dict):
            for year, value in result.items():
                if isinstance(value, dict):
                    for col, val in value.items():
                        data_dict[year][col] = val
                else:
                    print(f"Unexpected data format for year {year}: {value}")
        else:
            print(f"Unexpected data format: {result}")

    df = pd.DataFrame.from_dict(data_dict, orient='index')
    df.index.name = 'Year'
    df.reset_index(inplace=True)

    # Plotting the results
    plot_manager = MatplotlibPlotManager(df)
    plot_manager.plot_all_regressions('Year')
