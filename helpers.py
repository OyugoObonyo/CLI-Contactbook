"""
A module with helper functions
"""
import sqlite3

def exits(boolean):
    """
    exits - changes a boolean's value to false
    Return: converted boolean
    """
    boolean = False
    return boolean


def create_db():
    """
    create_db - creates a connection to the database
    Return: connection object
    """
    conn = sqlite3.connect('contacts.db')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    email TEXT UNIQUE)
    """)
    return conn

def check_db(cursor, name):
    """
    check_db - checks if a particular name is present in the db
    Return: true if name is in db and false if not
    """
    result = cursor.execute("SELECT * FROM contacts WHERE name = ?", (name, )).fetchone()
    if result is None:
        print(f"{name} is not saved in your phonebook")
        return 1
    return 0 
    