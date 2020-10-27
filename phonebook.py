import logger

repertoire = {}


def create_contact():
    """
    Fonction créant un contact en demandant à l'utilisateur de saisir ses données
    :return: Le contact
    """
    contact = {
        "Nom": input("Prénom : "),
        "Numéro": input("Numéro : "),
        "Favoris": input("Favori (True or False) : "),
    }
    return contact


def add_contact(rep, contact):
    """
    Ajoute le contact dans le répertoire
    :param rep: Le répertoire dans lequel on veux mettre le contact
    :param contact: Le contact qu'on veut mettre dans le répertoire
    :return: Rien
    """
    logger.write_log("add_contact")
    number = contact["Numéro"]
    rep[number] = contact


def get_names(rep):
    """
    Récupère tout les noms du répertoire et les tri dans l'ordre alphabétique
    :param rep: Le répertoire dans lequelle on veut récuperer les noms et les trier
    :return: Rien
    """
    name_list = []
    for k in rep:
        contact = rep[k]
        name_list.append(contact["Nom"])
    name_list.sort()
    print(name_list)


def display_all(rep):
    """
    Affiche tout le répertoire
    :param rep: Le répertoire qu'on veut afficher
    :return: Rien
    """
    logger.write_log("display_all")
    for k in rep:
        print(rep[k])


def get_contact(phone_number, rep):
    """
    Retrouve le contact en fonction du numéro donné par l'utilisateur
    :param phone_number: Numéro du contact qu'on veut retrouver
    :param rep: Répertoire dans lequelle on veut chercher
    :return: Les coordonées du contact
    """
    logger.write_log("get_contact")
    for k in rep:
        if phone_number == k:
            return rep[k]


def console_print():
    """
    Affiche le répertoire complet, le nom des contacts trié dans l'ordre alphabétique et demande le numéro
    qu'on veut rechercher
    :return: Rien
    """
    print("")
    print("Liste des noms de l'annuaire")
    get_names(repertoire)
    print("")
    print("Liste de tout les contacts avec coordonées")
    display_all(repertoire)
    print("")
    wanted_number = input("Quelle numéro veux tu chercher ? ")
    print(f"Le numéro {wanted_number} correspond à : {get_contact(wanted_number, repertoire)}")
