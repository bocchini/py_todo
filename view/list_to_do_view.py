from controllers.to_do_controller import get_all


def get_all_to_do_list():
    print('*' * 30, '-' * 4, ' Lista de tarefas ', '-' * 4, '*' * 30)
    print(get_all())
    input('Digite qualquer tacla para voltar ao menu')
