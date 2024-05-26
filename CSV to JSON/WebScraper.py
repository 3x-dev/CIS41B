import csv
from collections import defaultdict
from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self, source=None):
        """
        Initializes the WebScraper with either a file, URL, or HTML content.
        """
        self.data = None
        if source:
            if source.endswith('.csv'):
                self.read_csv(source)
            else:
                self.load_source(source)

    def load_source(self, source):
        """
        Load HTML content from a file, URL, or an HTML string directly.
        """
        if source.startswith(('http://', 'https://')):
            response = requests.get(source)
            response.raise_for_status()
            html_content = response.text
        elif source.endswith('.html'):
            with open(source, 'r', encoding='utf-8') as file:
                html_content = file.read()
        else:
            html_content = source
        
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def read_csv(self, filepath):
        """
        Manually parses a CSV file and converts it into a dictionary.
        This method detects if the CSV has headers or not and handles accordingly.
        """
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            content = file.readlines()
            reader = csv.reader(content)
            first_row = next(reader)
            if any(not item.replace('.', '').isdigit() for item in first_row):
                headers = first_row
            else:
                headers = [f"Column_{i+1}" for i in range(len(first_row))]
                content.insert(0, ','.join(first_row))
            
            data = defaultdict(list)
            reader = csv.reader(content)
            next(reader)
            for row in reader:
                for i, value in enumerate(row):
                    data[headers[i]].append(value)
        self.data = data

    def to_dataframe(self):
        """
        Converts internal data dictionary into a DataFrame using pandas.
        """
        import pandas as pd
        return pd.DataFrame(self.data)
