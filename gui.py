import todo_functions
import PySimpleGUI as sg

label = sg.Text('Type in a todo')
input_box = sg.InputText(tooltip='Enter a todo',key = 'todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = todo_functions.get_todos()
            todos.append(values['todo'])
            todo_functions.write_todos(todos)
        case 'Edit':
            pass
        case 'Complete':
            pass
        case sg.WIN_CLOSED:
            break
print('Window has been closed')
window.close()
