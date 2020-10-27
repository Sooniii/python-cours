from datetime import datetime


def write_log(text):
    """
    Ecrit dans le fichier log les fonctions utilisé
    :param text: Nom de la fonction qui est utilisé
    :return: Rien
    """
    actual_time = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.now())

    f = open("phonebook.log", "a")
    f.write(f"{actual_time} : La fonction {text} a été utilisée\n")
    f.close()


def dump_log():
    """
    Ecrit le contenu du fichier log dans la console
    :return: Rien
    """
    try:
        f = open("phonebook.log", "r")
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
        f.close()
    except FileNotFoundError as e:
        print(f"File not found. {e}")
