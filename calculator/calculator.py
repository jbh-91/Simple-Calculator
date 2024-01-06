"""
TODO: Docstring
"""

from icecream import ic

class Calculator():

    def __init__(self) -> None:
        self.allowed_digits = "0123456789."

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
        Requires valid string as input.

        Allowed operations are + - / * ** and parentheses ( ) 
        
        Removes empty spaces.
        Changes "**" to "^", because "**" might mix up with the sign/operation "*"

        Order of execution is retained.
        """

        expression: str = expression.replace("**", "^").replace(" ", "") + "+"  

        number: float = 0
        sign: str = "+" 
        stack: list = []

        memory_index: int | None = None


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

            # Operation: Handle potentiation with higher precedence
            if current == "^":
                # Remember current sign and number
                stack.append(sign)
                stack.append(number)

                number = 0
                sign = current

                continue

            # Operation: Execute potentiation in after "^" was current
            if sign == "^":
                    last_stack_number = stack.pop()
                    last_stack_sign = stack.pop()

                    power = last_stack_number ** number

                    if last_stack_sign == "+":
                        stack.append(power)
                    elif last_stack_sign == "-":
                        stack.append(-power)
                    elif last_stack_sign == "*":
                        stack.append(stack.pop() * power)
                    elif last_stack_sign == "/":
                        stack.append(stack.pop() / power)
                    
                    number = 0
                    sign = current
                    
            
            # Operation: + - * /
            if current in "*/+-" or current == ")" or index == len(expression) - 1:
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
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
    tc = Calculator()
    ic(tc.calculate("2**2**2")) # TODO: Fix double potentiation