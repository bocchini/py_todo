from view.menu import start_screen
from view.add_to_do_list import add
from view.list_to_do_view import get_all_to_do_list
from view.remove_to_do_view import remove_to_do_list


while True:
    start_screen()
    option = input('Digite uma opção: ')
    if option.lower() == 'a':
        add()
        continue
    elif option.lower() == 'l':
        get_all_to_do_list()
        continue
    elif option.lower() == 'r':
        remove_to_do_list()
        continue
    elif option.lower() == 'v':
        print('D')
        pass
    elif option.lower() == 'r':
        print('D')
        pass
    elif option.lower() == 's':
        break
