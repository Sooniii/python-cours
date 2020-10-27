from datetime import datetime


def write_log(function):
    actual_time = str(datetime.now())
    f = open("phonebook.log", "a")
    f.write(f"{actual_time} : La fonction {function} a été utilisée\n")
    f.close()


def dump_log():
    f = open("phonebook.log", "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
