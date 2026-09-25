from toolkit.tokenization import tokenize
from toolkit.validation import calculator_validation
from toolkit.calculation import calculate


def expession_calculate(expression: str):
    calculator_validation(expression)
    return str(calculate(tokenize(expression)))
