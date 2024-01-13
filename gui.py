import todo_functions
import PySimpleGUI as sg
import time

sg.theme('DarkAmber')
clock = sg.Text('',key='Clock')
label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='Enter a todo',key = 'todo_input')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=todo_functions.get_todos(),
                      key='todos_list',
                      enable_events=True,
                      size=(45,10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['Clock'].update(value= time.strftime('%b %d, %Y %H:%M'))
    match event:
        case 'Add':
            todos = todo_functions.get_todos()
            todos.append(values['todo_input'])
            todo_functions.write_todos(todos)

            window['todos_list'].update(values=todos)
        case 'Edit':
            try:
                old_todo = values['todos_list'][0]
            except IndexError:
                sg.popup('Please select an item first',font=('Helvetica',20))
                continue
            new_todo = values['todo_input']
            todos = todo_functions.get_todos()
            index = todos.index(old_todo)
            todos[index] = new_todo
            todo_functions.write_todos(todos)
            window['todos_list'].update(values = todos)
        case 'Complete':
            try:
                todo_to_complete = values['todos_list'][0]
            except IndexError:
                sg.popup('Please select an item first',font=('Helvetica',24))
                continue
            todos = todo_functions.get_todos()
            todos.remove(todo_to_complete)
            todo_functions.write_todos(todos)
            window['todos_list'].update(values=todos)
            window['todo_input'].update(value='')
        case 'todos_list':
            window['todo_input'].update(value=values['todos_list'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
print('Window has been closed')
window.close()
