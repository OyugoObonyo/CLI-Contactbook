"""
A module that consists of the program's main application logic
"""
from manager import ContactManager
from sender import SendManager
from helpers import exits


sender = SendManager()
contact_book = ContactManager()

controls = {
    "save": contact_book.save,
    "delete" : contact_book.delete,
    "display" : contact_book.show_all,
    "retrieve" : contact_book.show,
    "edit" : contact_book.update,
    "count" : contact_book.count_all,
    "text" : sender.text,
    "email" : sender.mail_to
}


proceed = True
# contain program logic within a REPL loop
while proceed:
    action = input("CLI >> ")
    if action in controls:
        execute = controls[action]
        execute()
    elif action == "exit":
        proceed = exits(proceed)
    else:
        print("Please enter a valid command!")