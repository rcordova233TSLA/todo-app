import time
from todo_functions import get_todos,write_todos
ERROR_MESSAGE = '{}......try again.......'

now = time.strftime('%b %d, %Y %H:%M')
print(f'It is {now}')
while True:
    user_action = input('Type add (followed by the item), '
                        'show, edit (followed by the number),'
                        'complete (followed by the number)'
                        'or exit: ').strip()
    if user_action.startswith('add'):
        a_todo = ''.join([x.strip() for x in user_action.split('add') if x != ''])
        todo_list = get_todos()
        todo_list.append(a_todo)
        write_todos(todo_list)
    elif user_action.startswith('show'):
        todo_list = get_todos()
        for index, item in enumerate(todo_list):
            print(f'{index + 1}.{item}')
    elif user_action.startswith('edit'):
        try:
            num_edit = int(''.join(x for x in user_action.split('edit') if x != '')) - 1
        except ValueError:
            print(ERROR_MESSAGE.format('A number was not entered'))
            continue
        new_todo = input("What's the new todo: ")
        todo_list = get_todos()
        old_todo = todo_list[num_edit]
        todo_list[num_edit] = new_todo
        write_todos(todo_list)
        print(f"'{old_todo}' has been replaced with '{new_todo}'")
    elif user_action.startswith('complete'):
        todo_list = get_todos()
        try:
            num_complete = int(''.join([x.strip() for x in user_action.split('complete') if x != ''])) - 1
        except ValueError:
            print(ERROR_MESSAGE.format('A number was not entered'))
            continue
        try:
            completed_todo = todo_list[num_complete]
        except IndexError:
            print(ERROR_MESSAGE.format('The inputted number cannot be found'))
            continue
        todo_list = get_todos()
        todo_list.pop(num_complete)
        write_todos(todo_list)
        print(f"'{completed_todo}' has been removed....")
    elif 'exit' in user_action:
        break

print('Bye')
