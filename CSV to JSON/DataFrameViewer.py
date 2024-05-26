import tkinter as tk
from tkinter import ttk

class DataFrameViewer:
    def __init__(self, master, dataframe):
        self.master = master
        self.dataframe = dataframe
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both')
        self.create_tabs()

    def create_tabs(self):
        tab1 = tk.Frame(self.notebook)
        self.notebook.add(tab1, text='Data')
        self.display_dataframe(tab1)

    def display_dataframe(self, frame):
        """
        Display DataFrame in a Tkinter frame.
        """
        for c, col_name in enumerate(self.dataframe.columns, start=1):
            tk.Label(frame, text=col_name, borderwidth=1, relief='solid', width=20, height=2, fg='blue', bg='lightgray').grid(row=0, column=c)
        
        for r, row in enumerate(self.dataframe.itertuples(index=False), start=1):
            for c, value in enumerate(row, start=1):
                tk.Label(frame, text=value, borderwidth=1, relief='solid', width=20, height=2, fg='black').grid(row=r + 1, column=c)
