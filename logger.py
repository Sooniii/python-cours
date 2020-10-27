from datetime import datetime


def write_log(text):
    #actual_time = str(datetime.now())
    actual_time = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.now())

    f = open("phonebook.log", "a")
    f.write(f"{actual_time} : La fonction {text} a été utilisée\n")
    f.close()


def dump_log():
    f = open("phonebook.log", "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
