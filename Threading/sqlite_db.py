import sqlite3
from WebScraperClass import WebScraper

class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def create_table(self, table_name, columns):
        # Sanitize column names to ensure they are valid SQL identifiers
        sanitized_columns = [self.sanitize_column_name(col) for col in columns if col.lower() != 'year']
        print(f"Sanitized Columns: {sanitized_columns}")
        columns_def = ', '.join([f'{col} REAL' for col in sanitized_columns])
        query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Year TEXT, {columns_def}
        )
        '''
        self.connection.execute(query)
        self.connection.commit()
        return sanitized_columns

    def sanitize_column_name(self, col):
        return col.replace(" ", "_").replace("<", "").replace(">", "").replace("(", "").replace(")", "").replace("-", "_").replace("*", "").replace("/", "").replace(".", "")

    def insert_data(self, table_name, columns, data):
        placeholders = ', '.join(['?' for _ in range(len(data[0]))])
        query = f'''
        INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})
        '''
        self.connection.executemany(query, data)
        self.connection.commit()

    def fetch_all_data(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        return rows

    def close(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    # Scrape the data
    url = 'https://gml.noaa.gov/aggi/aggi.html'
    scraper = WebScraper(url)
    headers, data = scraper.get_data()
    
    # Initialize and use the database
    db = SQLiteDB('aggi_data.db')
    db.connect()
    sanitized_columns = db.create_table('AGGI', headers)
    db.insert_data('AGGI', ['Year'] + sanitized_columns, [(row[0], *row[1:]) for row in data])
    print(db.fetch_all_data('AGGI'))
    db.close()
