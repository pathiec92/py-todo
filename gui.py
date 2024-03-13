import PySimpleGUI as g

label = g.Text("Todo List!")
ibox = g.InputText(tooltip="Enter the todo")

window = g.Window("My todo list", layout=[[label, ibox]])
window.read()
window.close()
