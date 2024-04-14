import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Updated to use 'string' instead of 'text'
    caption = soup.find('caption', string=lambda text: text and "Per capita CO2 emissions by country/territory" in text)
    if caption:
        return caption.find_parent('table')
    else:
        print("Table with specified caption not found. Check if the page structure has changed.")
        return None

def clean_and_organize_table(table):
    rows = table.find_all('tr')
    data = defaultdict(list)
    for row in rows:
        cells = row.find_all(['th', 'td'])
        if cells:
            country = cells[0].text.strip()
            emissions = cells[1].text.strip()  # Assuming emissions per capita are in the second column
            data['Country'].append(country)
            data['Emissions'].append(emissions)
    return data

def main():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
    html_content = fetch_page(url)
    if html_content:
        table = extract_table(html_content)
        if table:
            cleaned_data = clean_and_organize_table(table)
            print("Cleaned Data:", cleaned_data)
        else:
            print("No data to clean. Table was not found.")
    else:
        print("Failed to fetch webpage.")

if __name__ == "__main__":
    main()