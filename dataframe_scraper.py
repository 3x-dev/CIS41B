import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
import unittest
import sys

class WebScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    
    def extract_tags(self, tag_name):
        return self.soup.find_all(tag_name)
    
    def clean_data(self, tags):
        if not tags:
            return defaultdict(list)
        data_dict = defaultdict(list)
        headers = [th.get_text(strip=True) for th in tags[0].find_all('tr')[0].find_all('th')]
        for row in tags[0].find_all('tr')[1:]:
            cells = row.find_all('td')
            # Use the minimum of header count or cell count to avoid out-of-index issues
            min_count = min(len(headers), len(cells))
            for i in range(min_count):
                data_dict[headers[i]].append(cells[i].get_text(strip=True))
        return data_dict

def create_dataframe(data_dict):
    df = pd.DataFrame(data_dict)
    if df.empty:
        print("No data to display in DataFrame.")
    else:
        print(df)

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Unit Testing
class TestWebScraper(unittest.TestCase):
    def setUp(self):
        html_content = read_html_file('GHGEmissions.html')
        self.scraper = WebScraper(html_content)

    def test_extract_tags(self):
        tags = self.scraper.extract_tags('table')
        self.assertIsNotNone(tags)
        self.assertTrue(len(tags) > 0)

    def test_clean_data(self):
        tags = self.scraper.extract_tags('table')
        data = self.scraper.clean_data(tags)
        self.assertTrue(all(len(data[key]) > 0 for key in data))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
    else:
        html_content = read_html_file('GHGEmissions.html')
        scraper = WebScraper(html_content)
        tags = scraper.extract_tags('table')
        if tags:
            data_dict = scraper.clean_data(tags)
            create_dataframe(data_dict)
        else:
            print("No tables found in HTML content.")
