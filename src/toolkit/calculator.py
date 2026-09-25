from src.toolkit.tokenization import tokenize
from src.toolkit.validation import calculator_validation
from src.toolkit.calculation import calculate



def expession_calculate(expression: str) -> str:
    calculator_validation(expression)
    return str(calculate(tokenize(expression)))
