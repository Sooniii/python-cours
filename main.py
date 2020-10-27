import phonebook
import logger
import sys

program = True
args = sys.argv


while program:
    new_contact = phonebook.create_contact()
    phonebook.add_contact(phonebook.repertoire, new_contact)
    next_name = input("Rentré un nouveau numéro ? ")
    if next_name == "Non":
        program = False

phonebook.console_print()

for i in range(0, len(args)):
    if (args[i] == "-display") and (len(args) > i + 1):
        phonebook.get_contact(args[i + 1], phonebook.repertoire)

for i in range(0, len(args)):
    if args[i] == "-log":
        logger.dump_log()
