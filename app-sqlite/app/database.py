import sqlite3 

DB_NAME = "products.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

# puente entre FastAPI y SQLite.
