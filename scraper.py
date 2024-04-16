import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import unittest

def get_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.text

def extract_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    target_text = soup.find(lambda tag: tag.name in ["h2", "h3", "p"] and 'Per capita CO2 emissions by country/territory' in tag.text)
    if target_text:
        table = target_text.find_next('table')
        return table
    return None

def clean_tags(table):
    if not table:
        return defaultdict(list)
    data_dict = defaultdict(list)
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    for row in table.find_all('tr')[1:]:  # Skip the header row
        for header, td in zip(headers, row.find_all('td')):
            data_dict[header].append(td.get_text(strip=True))
    return data_dict

def print_cleaned_data(data_dict):
    for key, values in data_dict.items():
        print(f"{key}: {values}")

class TestCO2EmissionsScraping(unittest.TestCase):
    def test_scraping(self):
        url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
        html_content = get_html(url)
        table = extract_tags(html_content)
        self.assertIsNotNone(table, "Failed to find the CO2 emissions table.")
        data_dict = clean_tags(table)
        print_cleaned_data(data_dict)
        self.assertIn('Country / territory', data_dict)

if __name__ == '__main__':
    unittest.main()
