import phonebook
import logger

program = True


while program:
    new_contact = phonebook.create_contact()
    phonebook.add_contact(phonebook.repertoire, new_contact)
    next_name = input("Rentré un nouveau numéro ? ")
    if next_name == "Non":
        program = False

phonebook.console_print()
logger.dump_log()
