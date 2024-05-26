import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import csv

class WebScraper:
    def __init__(self, source=None):
        """
        Initializes the WebScraper with either a file, URL, HTML content, or CSV file path.
        """
        self.soup = None
        self.data = None
        if source:
            if source.endswith('.csv'):
                self.read_csv(source)
            else:
                self.load_source(source)

    def load_source(self, source):
        """
        Load HTML or CSV content from a file, URL, or a string directly.
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

    def extract_tags(self, tag_name):
        """
        Extracts all elements of a specific tag from HTML.
        """
        return self.soup.find_all(tag_name) if self.soup else []

    def clean_data(self, tags):
        """
        Converts the HTML of specified tags into a structured dictionary.
        """
        data_dict = defaultdict(list)
        headers = [th.get_text(strip=True) for th in tags[0].find_all('tr')[0].find_all('th')]
        for row in tags[0].find_all('tr')[1:]:
            cells = row.find_all('td')
            for i, cell in enumerate(cells):
                if i < len(headers):
                    data_dict[headers[i]].append(cell.get_text(strip=True))
        return data_dict

    def read_csv(self, filepath):
        """
        Read a CSV file and parse it into a structured dictionary.
        """
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = defaultdict(list)
            for row in reader:
                for header, value in row.items():
                    data[header].append(value)
        self.data = data