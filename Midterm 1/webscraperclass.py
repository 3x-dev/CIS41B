import requests
from bs4 import BeautifulSoup
from collections import defaultdict

class WebScraper:
    def __init__(self, source=None):
        """
        Initializes the WebScraper with either a file, URL, or HTML content.
        :param source: Could be a path to an HTML file, a URL, or raw HTML content.
        """
        if source:
            self.load_source(source)
        else:
            self.soup = None

    def load_source(self, source):
        """
        Load HTML content from a file, URL, or a HTML string directly.
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
        Extracts all elements of a specific tag.
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
            for i in range(min(len(headers), len(cells))):
                data_dict[headers[i]].append(cells[i].get_text(strip=True))
        return data_dict