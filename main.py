"""
A module that consists of the program's main application logic
"""
from manager import ContactManager
from helpers import exits, create_db
from dotenv import load_dotenv


contact_book = ContactManager()
controls = {
    "save": contact_book.save,
    "delete" : contact_book.delete,
    "all contacts" : contact_book.show_all,
    "show" : contact_book.show,
    "edit" : contact_book.update,
    "count" : contact_book.count_all,
}

# create database connection object
conn = create_db()
cursor = conn.cursor()

proceed = True
# contain program logic within a REPL loop
while proceed:
    action = input("CLI PHONEBOOK >> ")
    if action in controls:
        if action == "save":
            name = input("Contact name: ")
            email = input("Contact email: ")
            execute = controls[action]
            execute(conn, cursor, name, email)
        elif action == "delete":
            name = input("Enter name of contact you want to delete: ")
            execute = controls[action]
            execute(conn, cursor, name)
        elif action == "display":
            execute = controls[action]
            execute(cursor)
        elif action == "show":
            name = input("Enter name of contact you'd like to retrieve: ")
            execute = controls[action]
            execute(cursor, name)
        elif action == "edit":
            name = input("Enter name of contact you'd like to edit: ")
            execute = controls[action]
            execute(conn, cursor, name)
        elif action == "count":
            execute = controls[action]
            execute(cursor)
    elif action == "exit":
        conn.close()
        proceed = exits(proceed)
    else:
        print("Please enter a valid command!")