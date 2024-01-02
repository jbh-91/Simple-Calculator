"""
TODO: Docstring
"""

class Calculator():

    def __init__(self) -> None:
        self.allowed_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "9", "0", "."]
        self.allowed_operators = ["+", "-", "*", "/"]
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
        
    
    def parse_valid_input_to_list(self, validated_str: str) -> list:
        """
        Converts a validated string and returns a list of numbers, operations and paranthesis
        Requires valid input-string:
            - no division by zero
            - Needs an operator between numbers and aparanthesis
            - every paranthesis requries a open/closing-pair
        """

        str_to_parse = validated_str

        operation = []

        operation.append(validated_str[0])

        for el in validated_str[1::]:
            # After the first loop, operations[-1] would be two characters long and therefore not in self.allowed_digits
            # Thus it is required to look for the last character in the last list-element
            if el in self.allowed_digits and operation[-1][-1] in self.allowed_digits: 
                operation[-1] = operation[-1] + el

            # "-" (minus) is allowed after another operation and before an allowed_digit
            elif el in self.allowed_digits and operation[-1] == "-" and operation[-2] in self.allowed_operators:
                operation[-1] = operation[-1] + el

            # "*" is required for **
            elif el == "*" and operation[-1] == "*":
                operation[-1] = operation[-1] + el

            else:
                operation.append(el)

        return operation


    def calculate(self, operation: list) -> float:
        """
        Calculates the operation and returns the result as a float.
        Requires parsed input as a list 
        """
        return eval(operation) # temporary to set up tests
    


if __name__ == "__main__":
    calc = Calculator()
    print(calc.parse_valid_input_to_list("10+0.23023--100*(15-5)**2"))
