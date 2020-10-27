repertoire = {}


def create_contact():
    contact = {
        "Nom": input("Prénom : "),
        "Numéro": input("Numéro : "),
        "Favoris": input("Favori (True or False) : "),
    }
    return contact


def add_contact(rep, contact):
    number = contact["Numéro"]
    rep[number] = contact


def get_names(rep):
    name_list = []
    for k in rep:
        contact = rep[k]
        name_list.append(contact["Nom"])
    name_list.sort()
    print(name_list)


def display_all(rep):
    for k in rep:
        print(rep[k])


def get_contact(phone_number, rep):
    for k in rep:
        if phone_number == k:
            return rep[k]


def console_print():
    print("")
    print("Liste des noms de l'annuaire dans l'ordre alphabétique")
    get_names(repertoire)
    print("")
    print("Liste de tout les contacts avec coordonées")
    display_all(repertoire)
    print("")
    wanted_number = input("Quelle numéro veux tu chercher ? ")
    print(f"Le numéro {wanted_number} correspond à : {get_contact(wanted_number, repertoire)}")