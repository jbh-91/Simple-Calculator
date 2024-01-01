"""
TODO: Docstring
"""

class Calculator():

    def __init__(self) -> None:
        pass

    def calculate(self, valid_str_to_calculate: str) -> float:
        """
        Calculates the input-string and returns the result as a float.
        Requires valid input-string:
            - no division by zero
            - Needs an operator between numbers and aparanthesis
            - every paranthesis requries a open/closing-pair
        """
        return eval(valid_str_to_calculate) # temporary to set up tests

    def validate(self, str_to_validate: str) -> bool | str:
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

if __name__ == "__name__":
    pass
