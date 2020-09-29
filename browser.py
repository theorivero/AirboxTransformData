import PySimpleGUI as sg

sg.theme('LightGreen3')

from test import te

tasks=[]
#read(tasks)

layout = [
    [sg.Text('Arquivo P-Ctrl para Reev')],
    [sg.Text('Arquivo P-Ctrl',size=(8, 1)), sg.Input("", key="in"), sg.FileBrowse()],

   
    [sg.Button(button_text="Submit", key="sub")],

   



]

window = sg.Window('File Browser', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event =="sub":
        input=values['in']
        tasks, = te(input)
        
        


    elif event == None:
        break




window.Close()
