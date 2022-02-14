"""
A module that consists of the contact manager class
"""
from itertools import count
from helpers import create_db
from tabulate import tabulate


class ContactManager:
    """
    A class that handles actions related to the contacts in the phonebook
    """
    def save(self, conn, cursor, name, email):
        """
        save - saves a contact to the db
        @conn: database conection object
        @cursor: database cursor
        @contact: name of contact to be saved
        @email: email of contact to be saved
        """
        if name == "" or email == "":
            print("Name or email cannot be empty")
            return None
        cursor.execute("INSERT INTO contacts VALUES(NULL,?, ?)",(name, email))
        conn.commit()
        print(f"{name} has been added to your phonebook!")

    def show(self, conn, name):
        """
        show - shows a particular contact detail
        @name: name of contact to be displayed
        """
        print("Here is the number!")

    def show_all(self, cursor):
        """
        show_all - shows all the contacts in the database
        @conn: db connection cursor
        """
        contacts = cursor.execute("SELECT * FROM contacts").fetchall()
        print(tabulate(contacts, headers=["ContactID", "Name", "Email"]))

    def update(self, name, new_name, new_email):
        """
        updates a particular contact in the db
        @name: name of contact to be updated
        @new_name: new contact name
        @new_email: new contact email
        """
        print("number is updated!")

    def count_all(self, cursor):
        """
        shows the total count of contacts within the phonebook
        @cursor: database cursor
        """
        count = cursor.execute("SELECT COUNT(*) FROM contacts").fetchone()
        print(f"Total Number of contacts in your phonebook: {count[0]}")

    def delete(self, name):
        """
        delete - deletes a contact from the database
        @name: name of contact to be deleted from db
        """
        print("number is deleted!")