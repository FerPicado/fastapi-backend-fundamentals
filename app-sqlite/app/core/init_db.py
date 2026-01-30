
import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""
               
               CREATE TABLE IF NOT EXISTS products (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price REAL NOT NULL
               )
               """)
    conn.commit()
    conn.close()
    print("Database and table created.")
    
    if __name__ == "__main__":
        init_db()