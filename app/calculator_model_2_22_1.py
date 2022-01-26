

class CalcModel:

    ERROR_MESSAGE = "Error Occured."

    def evaluate_expression(self, expression):
        try:
            return str(eval(expression))
        except (ZeroDivisionError, TypeError):
            return self.__class__.ERROR_MESSAGE