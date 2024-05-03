import sqlite3
from bs4 import BeautifulSoup

class SQLiteManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        print(f"Connected to {self.db_path} successfully.")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            self.conn.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def query_builder(self, query_type, table_name, fields=None):
        queries = {
            "CREATE": lambda fields: f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{field} TEXT' for field in fields)})",
            "INSERT": lambda fields: f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})",
            "SELECT": lambda fields: f"SELECT * FROM {table_name}"
        }
        # Call the function from the dictionary with fields if needed
        return queries[query_type.upper()](fields if fields else [])

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    data = []
    table_bodies = soup.find_all('tbody')
    headers = [th.get_text().replace('#', '').strip() for th in table_bodies[2].find_all('td')]
    for tbody in table_bodies[3:]:
        for row in tbody.find_all('tr'):
            cols = row.find_all('td')
            data.append([col.text for col in cols])
    return headers, data

db_path = 'example.db'
html_path = 'Co2.html'

with SQLiteManager(db_path) as manager:
    headers, data = parse_html(html_path)
    create_query = manager.query_builder("CREATE", "Co2Data", headers)
    manager.execute_query(create_query)
    for row in data:
        insert_query = manager.query_builder("INSERT", "Co2Data", headers)
        manager.execute_query(insert_query, tuple(row))
    select_query = manager.query_builder("SELECT", "Co2Data")
    results = manager.execute_query(select_query)
    print(results)
