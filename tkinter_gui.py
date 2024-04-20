import tkinter as tk
from tkinter import ttk
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Cathy', 'David'],
    'Age': [25, 30, 22, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}
df = pd.DataFrame(data)

root = tk.Tk()
root.title('DataFrame Display')

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
notebook.add(tab1, text='DataFrame')
notebook.add(tab2, text='Headers')
notebook.add(tab3, text='Indices')
notebook.pack(expand=True, fill='both')

def display_dataframe(frame, dataframe):
    for r, row in enumerate(dataframe.itertuples(), start=1):
        for c, value in enumerate(row[1:], start=1):
            tk.Label(frame, text=value, borderwidth=1, relief='solid', width=15, height=2).grid(row=r, column=c)

def display_headers(frame, dataframe):
    for c, col_name in enumerate(dataframe.columns, start=1):
        tk.Label(frame, text=col_name, borderwidth=1, relief='solid', width=15, height=2, fg='blue').grid(row=0, column=c)
    for r, index in enumerate(dataframe.index, start=1):
        tk.Label(frame, text=index, borderwidth=1, relief='solid', width=15, height=2, fg='blue').grid(row=r, column=0)

def display_indices(frame, dataframe):
    tk.Label(frame, text="Index", borderwidth=1, relief='solid', width=15, height=2, fg='green').grid(row=0, column=0)
    for r, index in enumerate(dataframe.index, start=1):
        tk.Label(frame, text=index, borderwidth=1, relief='solid', width=15, height=2).grid(row=r, column=0)
    for c, col_name in enumerate(dataframe.columns, start=1):
        tk.Label(frame, text=col_name, borderwidth=1, relief='solid', width=15, height=2).grid(row=0, column=c)

display_dataframe(tab1, df)
display_headers(tab2, df)
display_indices(tab3, df)

root.mainloop()
