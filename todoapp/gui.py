import functions
import FreeSimpleGUI as sg


label = sg.Text("WriType in a to-do: ")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box, add_button]])
window.read()
window.close()