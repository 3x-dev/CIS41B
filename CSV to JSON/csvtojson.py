import tkinter as tk
from WebScraper import WebScraper
from DataFrameViewer import DataFrameViewer

def main():
    root = tk.Tk()
    root.title('CSV Data Viewer')

    scraper = WebScraper('AsciiFreq.csv')
    df = scraper.to_dataframe()

    viewer = DataFrameViewer(root, df)
    jsonCSV = df.to_json()
    print(jsonCSV)

    root.mainloop()

if __name__ == "__main__":
    main()
