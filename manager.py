"""
A module that consists of the contact manager class
"""
from tabulate import tabulate
from helpers import check_db
from sqlite3 import IntegrityError


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
        try:
            if name == "" or email == "":
                print("Name or email cannot be empty")
                return None
            cursor.execute("INSERT INTO contacts VALUES(NULL,?, ?)",(name, email))
            conn.commit()
        except IntegrityError:
            print("A contact with a similar name or email already exists")
            return None
        print(f"{name} has been added to your phonebook!")

    def show(self, cursor, name):
        """
        show - shows a particular contact detail
        @cursor: db cursor object
        @name: name of contact to be displayed
        """
        if name == "":
            print("Name cannot be empty")
            return None
        check = check_db(cursor=cursor, name=name)
        if check == 1:
            return None
        # append comma after name to make it a tuple
        contact = cursor.execute("SELECT * FROM contacts WHERE name = ?", (name, )).fetchall()
        if contact == []:
            print(f"{name} is not in your contactbook")
        else:
            print(tabulate(contact, headers=["ContactID", "Name", "Email" ]))

    def show_all(self, cursor):
        """
        show_all - shows all the contacts in the database
        @conn: db connection cursor
        """
        contacts = cursor.execute("SELECT * FROM contacts").fetchall()
        if contacts == []:
            print("You haven't saved any contact yet")
            return None
        print(tabulate(contacts, headers=["ContactID", "Name", "Email"]))

    def update(self, conn, cursor, name):
        """
        updates a particular contact in the db
        @cursor: cursor object
        @name: name of contact to be updated
        @new_name: new contact name
        @new_email: new contact email
        """
        if name == "":
            print("Name cannot be empty")
            return None
        check = check_db(cursor=cursor, name=name)
        if check == 1:
            return None
        new_name = input("Set new name: ")
        new_email = input("Set new email: ")
        query = "UPDATE contacts SET name = ?, email = ? WHERE name = ?"
        args = (new_name, new_email, name)
        cursor.execute(query, args)
        conn.commit()
        print("Contact updated!")

    def count_all(self, cursor):
        """
        shows the total count of contacts within the phonebook
        @cursor: database cursor
        """
        count = cursor.execute("SELECT COUNT(*) FROM contacts").fetchone()
        print(f"Total Number of contacts in your phonebook: {count[0]}")

    def delete(self, conn, cursor, name):
        """
        delete - deletes a contact from the database
        @name: name of contact to be deleted from db
        """
        if name == "":
            print("Name cannot be empty")
            return None
        check = check_db(cursor=cursor, name=name)
        if check == 1:
            return None
        query = "DELETE FROM contacts WHERE name = ?"
        args = (name, )
        cursor.execute(query, args)
        conn.commit()
        print(f"{name} has been deleted from your phonebook!")