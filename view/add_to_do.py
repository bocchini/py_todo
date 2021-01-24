from controllers.to_do_controller import add_to_do


def add():
    print('*' * 30, '-' * 4, ' Adicionar uma tarefa ', '-' * 4, '*' * 30)
    save = False
    while not save:
        title = input('Digite o titulo da tarefa: ').capitalize()
        to_do = input('Digite a tarefa: ').capitalize()
        want_to_save = input('Salvar a tarefa? (s/n) ')
        if want_to_save.lower() == 's':
            save = True
            do = add_to_do(title, to_do)
            print('Tarefa adicionada')
            print(do)



