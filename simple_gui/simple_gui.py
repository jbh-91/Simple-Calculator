import PySimpleGUI as sg

class NumButton(sg.Button):
    def __init__(self, *args, size: tuple=(3, 2)):
        super().__init__(*args, size=size)

class CalcButton(sg.Button):
    def __init__(self, *args, size: tuple=(3, 2), button_color="#1b2027"):
        super().__init__(*args, size=size, button_color=button_color)

prompt = ""

####
# GUI START
####

col1 = [
    [sg.Text(prompt, text_color="#000000", font = ("Arial", 14), background_color="#ffffff", size=(30, 2), key="-FIELD-")]
]

col2 = [
    [CalcButton("DEL", size=(26,2), button_color="#ff2200")]
]

col3 = [
    [CalcButton("1/x"), CalcButton("x²"), CalcButton("√x"), CalcButton("/")]
]

col4 = [
    [NumButton("7"), NumButton("8"), NumButton("9"), CalcButton("*")]
]

col5 = [
    [NumButton("4"), NumButton("5"), NumButton("6"), CalcButton("-")]
]

col6 = [
    [NumButton("1"), NumButton("2"), NumButton("3"), CalcButton("+")]
]

col7 = [
    [CalcButton("."), NumButton("0"), CalcButton("=", size=(11,2), button_color="#ff2200")]
]

layout = [
    [sg.Column(col1)],
    [sg.Column(col2)],
    [sg.Column(col3)],
    [sg.Column(col4)],
    [sg.Column(col5)],
    [sg.Column(col6)],
    [sg.Column(col7)]
]

window = sg.Window("Simple Calculator", layout, size=(275, 440))

####
# GUI END
####

while True:
    event, values = window.read()

    match event:
        case sg.WIN_CLOSED:
            break
        case "=":
            prompt = str(eval(prompt))  # only temporary 
            window["-FIELD-"].update(prompt)
        case "DEL":
            prompt = ""
            window["-FIELD-"].update(prompt)
        case _: 
            prompt = prompt + event
            window["-FIELD-"].update(prompt)

window.close()
