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

def check_db(conn, name):
    """
    check_db - checks if a particular name is present in the db
    Return: true if name is in db and false if not
    """
    conn.execute("""
    """)
    