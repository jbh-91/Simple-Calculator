import PySimpleGUI as sg
import calculator.calculator as calc

class NumButton(sg.Button):
    def __init__(self, *args, size: tuple=(3, 2)):
        super().__init__(*args, size=size)

class CalcButton(sg.Button):
    def __init__(self, *args, size: tuple=(3, 2), button_color="#1b2027"):
        super().__init__(*args, size=size, button_color=button_color)

calc = calc.Calculator()

prompt = ""
operators = "()*/-+"
digits = "0123456789."

####
# GUI START
####

col1 = [
    [sg.Text(prompt, text_color="#000000", font = ("Arial", 14), background_color="#ffffff", size=(30, 2), key="-FIELD-")]
]

col2 = [
    [CalcButton("("), CalcButton(")"), CalcButton("←", button_color="#882200"), CalcButton("DEL", button_color="#ff2200")]
]

col3 = [
    [CalcButton("x²"), CalcButton(f"x**n"), CalcButton("n√x"), CalcButton("/")]
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
        
        # Deletion and Backspace
        case "DEL":
            prompt = ""
            window["-FIELD-"].update(prompt)
        case "←":
            prompt = prompt[0:-1]
            window["-FIELD-"].update(prompt)

        # Resolve expression
        case "=":
            result = calc.calculate(prompt)
            prompt = str(result)
            window["-FIELD-"].update(prompt)

        # square exponent
        case "x²":
            prompt = prompt + "**2"
            window["-FIELD-"].update(prompt)

        # nth exponent
        case "x**n":
            n = sg.popup_get_text("Please enter the nth exponent: ", title="Potentiation")
            prompt = prompt + f"**{n}"
            window["-FIELD-"].update(prompt)

        # radicals / roots
        case "n√x":
            n = sg.popup_get_text("Please enter the nth root: ", title="Radical")
            prompt = prompt + f"**(1/{n})"
            window["-FIELD-"].update(prompt)
        
        # Use Buttontext as input
        case _: 
            prompt = prompt + event
            window["-FIELD-"].update(prompt)

window.close()
