from model.to_do_model import add, get_all_to_do, remove


def add_to_do(title, to_do=None):
    do = add(title, to_do)
    return do


def get_all():
    to_do = get_all_to_do()
    return to_do


def remove_to_do(to_do):
    list_to_do = get_all_to_do()

    if to_do in list_to_do:
        del (list_to_do[to_do])
        remove(list_to_do)
        return 'Item removido'
    return 'Não encontrado'

