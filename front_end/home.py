import PySimpleGUI as sg
import sys 
import os
sys.path.append(os.path.abspath("E:/work/coformatique/my_Guestbook/back_end"))
from login_create import login, create

#create layout
layout = [
        [sg.Text("Login or create an account")], 
        [sg.Text("username:",size = (15,1)),sg.InputText()],
        [sg.Text("password:",size = (15,1)),sg.InputText()],
        [sg.Button("login"), sg.Button("create account")]
        ]

# Create the window
window = sg.Window("Home", layout)

while True:
    #listen for events
    event, values = window.read() 
    if event == "login":
        login(values)
    elif event == "create account":
        create(values)
    elif event == sg.WIN_CLOSED:
        break
window.close()