import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
import unittest
import sys

class WebScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    
    def extract_tags(self, tag_name):
        """ Extracts and returns all tags with the given name from the parsed HTML. """
        return self.soup.find_all(tag_name)
    
    def clean_data(self, tags):
        """ Cleans the extracted tags and organizes the data into a defaultdict. """
        data_dict = defaultdict(list)
        for row in tags[0].find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 7:
                data_dict['Year'].append(cells[0].get_text(strip=True))
                data_dict['Month'].append(cells[1].get_text(strip=True))
                data_dict['Decimal'].append(cells[2].get_text(strip=True))
                data_dict['Average'].append(cells[3].get_text(strip=True))
                data_dict['Interpolated'].append(cells[4].get_text(strip=True))
                data_dict['Trend'].append(cells[5].get_text(strip=True))
                data_dict['Days'].append(cells[6].get_text(strip=True))
        return data_dict

def create_dataframe(data_dict):
    """ Converts the dictionary data into a Pandas DataFrame and prints it. """
    df = pd.DataFrame(data_dict)
    print(df)

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Unit Testing
class TestWebScraper(unittest.TestCase):
    def setUp(self):
        html_content = read_html_file('Co2.html')
        self.scraper = WebScraper(html_content)

    def test_extract_tags(self):
        tags = self.scraper.extract_tags('table')
        self.assertIsNotNone(tags)
        self.assertTrue(len(tags) > 0)

    def test_clean_data(self):
        tags = self.scraper.extract_tags('table')
        data = self.scraper.clean_data(tags)
        self.assertEqual(len(data['Year']), len(data['Month']))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
    else:
        html_content = read_html_file('Co2.html')
        scraper = WebScraper(html_content)
        tags = scraper.extract_tags('table')
        if tags:
            data_dict = scraper.clean_data(tags)
            create_dataframe(data_dict)
