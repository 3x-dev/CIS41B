import csv

class CSVReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def to_dataframe(self):
        data = []
        with open(self.filepath, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                if row:
                    data.append(row)

        df = {header: [] for header in headers}
        for row in data:
            for header, value in zip(headers, row):
                df[header].append(value)

        return df
