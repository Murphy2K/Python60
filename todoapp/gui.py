import functions
import FreeSimpleGUI as sg
import time

import os
#Teeb todos.txt faili KUI seda ei ole olemas.
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("LightBrown13")

clock = sg.Text("", key="clock")
label = sg.Text("Sisesta to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Lisa", key="Add", mouseover_colors="LightBlue2", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                    enable_events=True, size=[45,10])
edit_button = sg.Button("Muuda", key="Edit")
complete_button = sg.Button("Valmis", key="Complete")
exit_button = sg.Button("Välju", key="Exit")


"""
nuppudele ei pea lisama key=...  kui all see case on sama sõna mis on nupul nimeks
"""


window = sg.Window("My To-Do app", 
                    layout=[[clock],
                        [label], 
                        [input_box, add_button], 
                        [list_box, edit_button, complete_button ],
                        [exit_button] ], 
                    font=("Helvetica", 20))


while True:
    event, values = window.read(timeout=800)
    window["clock"].update(value=time.strftime("%d %B %Y %H:%M:%S"))
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"  # Peab võtma sisendist, mitte listboxist!
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todos_to_edit = values["todos"][0]  # Võtab valitud elemendi
                new_todo = values["todo"] + "\n"    # Võtab sisendiväljast uue väärtuse

                todos = functions.get_todos()
                index = todos.index(todos_to_edit)  # Leiab indeksi listis
                todos[index] = new_todo             # Asendab uue väärtusega
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo to edit")

                
        
        case "Complete":
            try:
                todos_to_complete = values["todos"][0]  # Võtab valitud elemendi
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a todo to complete")


        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        
        case sg.WIN_CLOSED:
            break

        
window.close()