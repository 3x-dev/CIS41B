import requests
from bs4 import BeautifulSoup
from collections import defaultdict

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
    
    def fetch_html(self):
        """ Fetches the HTML content from the specified URL and parses it with BeautifulSoup. """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return None
    
    def extract_tags(self, tag_name):
        """ Extracts and returns all tags with the given name from the fetched HTML. """
        try:
            if self.soup is None:
                return None
            return self.soup.find_all(tag_name)
        except Exception as e:
            print(f"Error extracting tags: {e}")
            return None
    
    def clean_data(self, tags):
        """ Cleans the extracted tags and organizes the data into a defaultdict. """
        data_dict = defaultdict(list)
        try:
            for tag in tags:
                data_dict[tag.name].append(tag.get_text(strip=True))
            return data_dict
        except Exception as e:
            print(f"Error cleaning data: {e}")
            return defaultdict(list)

def scrape_co2_emissions(url):
    """ Uses the WebScraper class to scrape and display CO2 emissions data from the given URL. """
    scraper = WebScraper(url)
    scraper.fetch_html()
    tables = scraper.extract_tags('table')
    co2_table = None
    for table in tables:
        if 'Country' in str(table):
            co2_table = table
            break
    if co2_table:
        data = scraper.clean_data([co2_table]) 
        for key, value in data.items():
            print(f"{key}: {value[:3]}")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
    scrape_co2_emissions(url)
