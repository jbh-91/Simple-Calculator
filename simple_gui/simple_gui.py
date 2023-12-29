import PySimpleGUI as sg

class FButton(sg.Button):
    def __init__(self, *args):
        super().__init__(*args, size=(3, 2))


col1 = [
    [sg.Text(key="-FIELD-")]
]

col2 = [
    [FButton("%"),FButton("CE"), FButton("C"), FButton("DEL")]
]

col3 = [
    [FButton("1/x"), FButton("x²"), FButton("√x"), FButton("/")]
]

col4 = [
    [FButton("7"), FButton("8"), FButton("9"), FButton("*")]
]

col5 = [
    [FButton("4"), FButton("5"), FButton("6"), FButton("-")]
]

col6 = [
    [FButton("1"), FButton("2"), FButton("3"), FButton("+")]
]

col7 = [
    [FButton("+/-"), FButton("0"), FButton("."), FButton("=")]
]

layout = [
    [sg.Text(background_color='#ffffff', size=(30, 3))],
    [sg.Column(col1)],
    [sg.Column(col2)],
    [sg.Column(col3)],
    [sg.Column(col4)],
    [sg.Column(col5)],
    [sg.Column(col6)],
    [sg.Column(col7)]
]

window = sg.Window('Simple Calculator', layout, size=(275, 480))


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

#    switch:
#        
#    case:
#        

window.close()