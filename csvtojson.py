import tkinter as tk
from tkinter import ttk
import pandas as pd
from updatedwebscraperclass import WebScraper

def display_dataframe(frame, dataframe):
    for r, row in enumerate(dataframe.itertuples(), start=1):
        for c, value in enumerate(row[1:], start=1):
            tk.Label(frame, text=value, borderwidth=1, relief='solid', width=20, height=2).grid(row=r, column=c)

def main():
    root = tk.Tk()
    root.title('CSV Data Viewer')

    notebook = ttk.Notebook(root)
    tab1 = tk.Frame(notebook)
    notebook.add(tab1, text='Data')
    notebook.pack(expand=True, fill='both')

    csv_reader = WebScraper('Dwarfs.csv')
    data_dict = csv_reader.to_dataframe()
    df = pd.DataFrame(data_dict)
    
    jsonCSV = df.to_json()
    print(jsonCSV)

    display_dataframe(tab1, df)

    root.mainloop()

if __name__ == "__main__":
    main()
