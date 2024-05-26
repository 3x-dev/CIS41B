from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
from webscraperclass import WebScraper

def process_data(data_dict):
    """
    Processes the data dictionary into a pandas DataFrame and performs aggregation.
    """
    df = pd.DataFrame(data_dict)
    df['Greenhouse gas emissions from agriculture'] = pd.to_numeric(df['Greenhouse gas emissions from agriculture'], errors='coerce')
    result_df = df.groupby('Entity')['Greenhouse gas emissions from agriculture'].mean().reset_index()
    result_df.columns = ['Country', 'Calculated Annual Average']
    return result_df

def main():
    scraper = WebScraper('GHGEmissions.html')
    tags = scraper.extract_tags('table')
    if tags:
        data_dict = scraper.clean_data(tags)
        result_df = process_data(data_dict)
        print(result_df)
    else:
        print("No tables found in HTML content.")

if __name__ == "__main__":
    main()
