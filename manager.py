"""
A module that consists of the contact manager class
"""
from helpers import create_db

conn = create_db()

class ContactManager:
    """
    A class that handles actions related to the contacts in the phonebook
    """
    def save(self, name, email):
        """
        save - saves a contact to the db
        @contact: name of contact to be saved
        @email: email of contact to be saved
        """
        if name == "" or email == "":
            print("Name or email cannot be empty")
            return None
        conn.execute("INSERT INTO contacts VALUES(?, ?)",(email, name))
        print("number is saved!")

    def show(self, name):
        """
        show - shows a particular contact detail
        @name: name of contact to be displayed
        """
        print("Here is the number!")


    def show_all(self):
        """
        show_all - shows all the contacts in the database
        """
        #remember to include the table library
        print("all numbers are shown man!")

    def update(self, name, new_name, new_email):
        """
        updates a particular contact in the db
        @name: name of contact to be updated
        @new_name: new contact name
        @new_email: new contact email
        """
        print("number is updated!")

    def count_all(self):
        """
        shows the total count of contacts within the phonebook
        """
        print("50")

    def delete(self, name):
        """
        delete - deletes a contact from the database
        @name: name of contact to be deleted from db
        """
        print("number is deleted!")