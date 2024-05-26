import sqlite3

def create_database(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, email) VALUES
        ('Henry', 'henry@example.com'),
        ('Charles', 'charles@example.com'),
        ('Adam', 'adam@example.com')
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database('Database.db')
