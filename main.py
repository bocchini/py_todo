from view.menu import start_screen
from view.add_to_do import add
from view.list_to_do import get_all_to_do_list


while True:
    start_screen()
    option = input('Digite uma opção: ')
    if option.lower() == 'a':
        add()
    elif option.lower() == 'l':
        print('L')
        get_all_to_do_list()
    elif option.lower() == 'f':
        print('F')
        pass
    elif option.lower() == 'd':
        print('D')
        pass
    elif option.lower() == 's':
        break
