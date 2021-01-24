FILE = 'todo.txt'


def add(do):
    with open(FILE, 'a+') as file:
        file.write('@'.join(str(line) for line in do))
        return do


def get_all_to_do():
    with open(FILE, 'r') as file:
        all_to_do = file.read()
        return all_to_do
