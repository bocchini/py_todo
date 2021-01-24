from model.to_do_model import add, get_all_to_do


def add_to_do(title, to_do=None):
    to_do = ([title, to_do])
    do = add(to_do)
    return do


def get_all():
    to_do = get_all_to_do()
    to_do = to_do.split('@')
    return to_do

