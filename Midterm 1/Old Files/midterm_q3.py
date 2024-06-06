import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
import sys

class WebScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    
    def extract_tags(self, tag_name):
        return self.soup.find_all(tag_name)
    
    def clean_data(self, tags):
        data_dict = defaultdict(list)
        headers = [th.get_text(strip=True) for th in tags[0].find_all('tr')[0].find_all('th')]
        for row in tags[0].find_all('tr')[1:]:
            cells = row.find_all('td')
            for i in range(min(len(headers), len(cells))):
                data_dict[headers[i]].append(cells[i].get_text(strip=True))
        return data_dict

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def process_data(data_dict):
    df = pd.DataFrame(data_dict)
    
    df['Greenhouse gas emissions from agriculture'] = pd.to_numeric(df['Greenhouse gas emissions from agriculture'], errors='coerce')
    
    result_df = df.groupby('Entity')['Greenhouse gas emissions from agriculture'].mean().reset_index()
    result_df.columns = ['Country', 'Calculated Annual Average']
    return result_df

def main():
    html_content = read_html_file('GHGEmissions.html')
    scraper = WebScraper(html_content)
    tags = scraper.extract_tags('table')
    if tags:
        data_dict = scraper.clean_data(tags)
        result_df = process_data(data_dict)
        print(result_df)
    else:
        print("No tables found in HTML content.")

if __name__ == "__main__":
    main()
