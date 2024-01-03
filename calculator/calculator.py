"""
TODO: Docstring
"""

from icecream import ic

class Calculator():

    def __init__(self) -> None:
        self.allowed_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        self.ordered_operators = ["^", "*", "/", "+", "-"]
        self.allowed_paranthesis = ["(", ")"]


    def validate_input(self, str_to_validate: str) -> bool | str:
        """
        Validates an input-string if it can be calculated.
        Returns True if the string is valid.
        Returns a string with an error-message if string is invalid
        """

        if not str_to_validate.count("(") == str_to_validate.count(")"):
            return "Input invalid - missing pair in parantesis!"
        
        # TODO: Lookup best practice and rework
        try:
            eval(str_to_validate)
        except ZeroDivisionError:
            return f"{ZeroDivisionError}: division by zero!"
        except NameError:
            return f"{TypeError}: no letters allowed"
        except TypeError:
            return f"{TypeError}: missing an operator between numbers and parantesis!"
        except SyntaxError:
            return f"{SyntaxError}: missing pair in paranthesis!"
        

    def calculate(self, expression: str) -> float:
        """
        Calculates the operation and returns the solution as a float.
        Requires valid string as input
        """

        expression: str = expression.replace("**", "^") + "+"  # Required for last iteration

        number: float = 0
        sign: str = "+" 
        stack: list = []

        memory_index: int = None


        for index, current in enumerate(expression):
            #ic(current, number, sign, stack)
            # Numbers of type float or int
            if current in self.allowed_digits: 
                if memory_index == None:
                    if expression[index + 1] in self.allowed_digits:
                        memory_index = index
                    else: 
                        number = float(current)
                elif expression[index + 1] not in self.allowed_digits:
                    number = float(expression[memory_index:index + 1])
                    memory_index = None
                else:
                    continue
            
            # Handling opening parantheses with a stack
            if current == "(":
                stack.append(sign)
                stack.append("(")
                sign = "+"
            
            # Operations
            if current in self.ordered_operators or current == ")" or index == len(expression) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                elif sign == "^":
                    stack.append(stack.pop() ** number)
                elif sign == "/":
                    stack.append(stack.pop() / number)

                if current == ")":
                    number = 0
                    element = stack.pop()
                    while element != "(":
                        number += element
                        element = stack.pop()
                    sign = stack.pop()
                else:
                    number = 0
                    sign = current

        else:
            solution = sum(stack)
            return solution
    


if __name__ == "__main__":
    calc = Calculator()
    #print(calc.calculate("2+5"))
    #print(calc.calculate("4*(3+2)"), "=? 20")
    #print(calc.calculate("4*(3+-2)"))
    #print(calc.calculate("4**2"))
    print(calc.calculate("10*(2+5)"), "=? 70")
    print(calc.calculate("10*(2+5)--100"), "=? -30")
    print(calc.calculate("-100*(15-5)"), "=? -1000")
    print(calc.calculate("(10*(2+5)--100*(15-5))"), "=? -930")
    print(calc.calculate("(10*(2+5)--100*(15-5))**2"), "=? 864900")
    print(calc.calculate("4**(1/2)"), "=? 2")
    print(calc.calculate("10+15*(3-8)**5"), "=? -46865") # Somethings wrong with potentiation and * before and after a paranthesis **

    # TODO: ** and ^ are treated in same order as every other operator; Stack looks back, potentiation needs to look forward