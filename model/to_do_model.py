import json
from ast import literal_eval

FILE = 'todo.txt'


def add(title, do):
    do_bd = get_all_to_do()
    do_bd[title] = do
    with open(FILE, 'w+') as file:
        json.dump(do_bd, file)
        return do


def get_all_to_do():
    with open(FILE, 'r') as file:
        all_to_do = file.read()
        all_to_do = literal_eval(all_to_do)
        return all_to_do


def remove(list_to_do):
    with open(FILE, 'w+') as file:
        file.write(json.dumps(list_to_do))
