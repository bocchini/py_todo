from controllers.to_do_controller import remove_to_do


def remove_to_do_list():
    print('*' * 30, '-' * 4, ' Remover qual tarefa ', '-' * 4, '*' * 30)
    to_do = input('Digite o título da tarefa: ').capitalize()
    remove_to_do(to_do)
