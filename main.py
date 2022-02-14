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
    "display" : contact_book.show_all,
    "retrieve" : contact_book.show,
    "edit" : contact_book.update,
    "count" : contact_book.count_all,
}

# create database connection object
conn = create_db()

proceed = True
# contain program logic within a REPL loop
while proceed:
    action = input("CLI PHONEBOOK >> ")
    if action in controls:
        if action == "save":
            name = input("Contact name: ")
            email = input("Contact email: ")
            execute = controls[action]
            execute(conn, name, email)
        elif action == "delete":
            name = input("Enter name of contact you want to delete: ")
            execute = controls[action]
            execute(name)
        elif action == "display":
            execute = controls[action]
            execute(conn)
        elif action == "retrieve":
            name = input("Enter name of contact you'd like to retrieve: ")
            execute = controls[action]
            execute(name)
        elif action == "edit":
            name = input("Enter name of contact you'd like to edit: ")
            new_name = input("Set new name: ")
            new_email = input("Set new email: ")
            execute = controls[action]
            execute(name, new_email, new_email)
        elif action == "count":
            execute = controls[action]
            execute()
    elif action == "exit":
        conn.close()
        proceed = exits(proceed)
    else:
        print("Please enter a valid command!")