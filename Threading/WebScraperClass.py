import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def parse_table(self):
        if not self.soup:
            raise Exception("No page content fetched. Call fetch_page() first.")
        
        table = self.soup.find('table', class_='table table-bordered table-condensed table-striped table-header')
        if not table:
            raise Exception("The table with the specified class was not found.")

        header_rows = table.find_all('tr')
        if len(header_rows) < 2:
            raise Exception("The table does not contain enough header rows.")

        headers = [th.get_text(separator=" ") for th in header_rows[1].find_all('th')][:7]

        rows = table.find('tbody').find_all('tr')
        data = []
        for row in rows:
            columns = row.find_all('td')
            row_data = [columns[i].get_text() for i in range(7)]
            data.append(row_data)
        return headers, data

    def get_data(self):
        self.fetch_page()
        headers, data = self.parse_table()
        return headers, data

if __name__ == "__main__":
    url = 'https://gml.noaa.gov/aggi/aggi.html'
    scraper = WebScraper(url)
    headers, data = scraper.get_data()
    print(headers)
    print(data)
