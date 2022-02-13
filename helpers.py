"""
A module with helper functions
"""
import sqlite3

def exits(boolean):
    """
    changes a booleans value to false
    """
    boolean = False
    return boolean


def create_db():
    conn = sqlite3.connect('contacts.db')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT)
    """)
    
    return conn

catch = create_db()
print(catch)