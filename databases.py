import sqlite3

class SQLiteManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            print(f"Connected to {self.db_path} successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        """Disconnect from the SQLite database."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        """Execute a SQL query with optional parameters."""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            else:
                self.conn.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def query_builder(self, query_type, table_name, fields=None, values=None):
        """Build SQL queries dynamically."""
        query = ""
        if query_type.upper() == "CREATE":
            query = f"CREATE TABLE {table_name} ({', '.join(fields)})"
        elif query_type.upper() == "INSERT":
            placeholders = ', '.join(['?' for _ in values])
            query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"
        elif query_type.upper() == "SELECT":
            query = f"SELECT * FROM {table_name}"
        elif query_type.upper() == "UPDATE":
            set_clause = ', '.join([f"{field} = ?" for field in fields])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {values[0]} = {values[1]}"
        elif query_type.upper() == "DELETE":
            query = f"DELETE FROM {table_name} WHERE {fields[0]} = ?"
        return query

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# Example usage
db_path = 'example.db'
with SQLiteManager(db_path) as manager:
    create_query = manager.query_builder("CREATE", "Users", ["id INTEGER PRIMARY KEY", "name TEXT"])
    manager.execute_query(create_query)
    insert_query = manager.query_builder("INSERT", "Users", ["id", "name"], [1, "John Doe"])
    manager.execute_query(insert_query, (1, "John Doe"))
    select_query = manager.query_builder("SELECT", "Users")
    results = manager.execute_query(select_query)
    print(results)
