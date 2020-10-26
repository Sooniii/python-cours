repertoire = {}
program = True


def create_contact():
    contact = {
        "name": input("Prénom : "),
        "phone_number": input("Numéro : "),
        "is_favorite": input("Favori (True or False) : "),
    }
    return contact


def add_contact(rep, contact):
    number = contact["phone_number"]
    rep[number] = contact


def get_names(rep):
    name_list = []
    for k in rep:
        contact = rep[k]
        name_list.append(contact["name"])
    name_list.sort()
    print(name_list)


while program:

    new_contact = create_contact()
    add_contact(repertoire, new_contact)
    next_name = input("Rentré un nouveau numéro ? ")
    if next_name == "Non":
        program = False

get_names(repertoire)



