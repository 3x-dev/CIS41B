import tkinter as tk
from tkinter import ttk
import pandas as pd
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
    
    def extract_tags(self, tag_name):
        return self.soup.find_all(tag_name)
    
    def clean_data(self, tags):
        data_dict = {}
        headers = [th.get_text(strip=True) for th in tags[0].find_all('tr')[0].find_all('th')]
        for row in tags[0].find_all('tr')[1:]:
            cells = row.find_all('td')
            for i, cell in enumerate(cells):
                if headers[i] not in data_dict:
                    data_dict[headers[i]] = []
                data_dict[headers[i]].append(cell.get_text(strip=True))
        return data_dict

def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def process_data(data_dict):
    df = pd.DataFrame(data_dict)
    agriculture_col = 'Greenhouse gas emissions from agriculture'
    df[agriculture_col] = pd.to_numeric(df[agriculture_col], errors='coerce')
    result_df = df.groupby('Entity')[agriculture_col].mean().reset_index()
    result_df.columns = ['Country', 'Calculated Annual Average']
    return result_df

def main():
    root = tk.Tk()
    root.title('GHG Emissions Data Viewer')

    notebook = ttk.Notebook(root)
    tab1 = tk.Frame(notebook)
    tab2 = tk.Frame(notebook)
    tab3 = tk.Frame(notebook)
    notebook.add(tab1, text='Data')
    notebook.add(tab2, text='Headers')
    notebook.add(tab3, text='Indices')
    notebook.pack(expand=True, fill='both')

    def display_dataframe(frame, dataframe):
        for r, row in enumerate(dataframe.itertuples(), start=1):
            for c, value in enumerate(row[1:], start=1):
                tk.Label(frame, text=value, borderwidth=1, relief='solid', width=20, height=2).grid(row=r, column=c)

    def display_headers(frame, dataframe):
        for c, col_name in enumerate(dataframe.columns, start=1):
            tk.Label(frame, text=col_name, borderwidth=1, relief='solid', width=20, height=2, fg='blue').grid(row=0, column=c)

    def display_indices(frame, dataframe):
        for r, index in enumerate(dataframe.index, start=1):
            tk.Label(frame, text=index, borderwidth=1, relief='solid', width=20, height=2, fg='green').grid(row=r, column=0)

    html_content = read_html_file('GHGEmissions.html')
    scraper = WebScraper(html_content)
    tags = scraper.extract_tags('table')
    data_dict = scraper.clean_data(tags)
    df = process_data(data_dict)

    display_dataframe(tab1, df)
    display_headers(tab2, df)
    display_indices(tab3, df)

    root.mainloop()

if __name__ == "__main__":
    main()
