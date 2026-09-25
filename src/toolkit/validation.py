import sys

def null_expression(expression: str):
    expression_no_space = expression.replace(" ", "")
    if expression_no_space == "":
        sys.stderr.write("Error: Null expression")
        sys.exit(2)


def unknown_symbol(expression: str):
    expression = expression.replace(" ", "")
    available_symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '%', '(', ')', '.')
    for symbol in expression:
        if symbol not in available_symbols:
            sys.stderr.write(f"Error: Unknown symbol \"{symbol}\"")
            sys.exit(2)

def missing_operand(expression: str):
    expression = expression.replace(" ", "")
    if expression[0] in ('*', '%', '/'):
        sys.stderr.write("Error: Missing operand")
        sys.exit(2)
    for part in ('+', '-', '*', '/', '%'):
        if part+')' in expression:
            sys.stderr.write("Error: Missing operand")
            sys.exit(2)
    for part in ('*', '/', '%'):
        if '('+part in expression:
            sys.stderr.write("Error: Missing operand")
            sys.exit(2)


def binary_operator(expression: str):
    expression = expression.replace(" ", "")
    if '///' in expression:
        sys.stderr.write("Error: Two binary operators")
        sys.exit(2)
    for part1 in ('--', '-+', '+-', '++', '*', '%', '/'):
        for part2 in ('*', '%'):
            if part1+part2 in expression or part2+part1 in expression:
                sys.stderr.write("Error: Two binary operators")
                sys.exit(2)
    for part1 in ('--', '-+', '+-', '++', '*', '%', '/'):
        for part2 in ('+', '-', '*', '%'):
            if part2+part1 in expression:
                sys.stderr.write("Error: Two binary operators")
                sys.exit(2)
    for part1 in ('--', '-+', '+-', '++'):
        for part2 in ('(', ')'):
            if part1+part2 in expression or part2+part1 in expression:
                sys.stderr.write("Error: Two binary operators")
                sys.exit(2)



def division_by_zero(expression: str):
    expression = expression.replace(" ", "")
    if '/0' in expression or '%0' in expression:
        sys.stderr.write("Error: Division by zero")
        sys.exit(2)


def undefined_measure(from_measure: str, to_measure: str, measures: list):
    is_found_from = False
    is_found_to = False
    for group in measures:
        if from_measure in group["measures"]:
            is_found_from = True
        if to_measure in group["measures"]:
            is_found_to = True
    if not (is_found_from and is_found_to):
        sys.stderr.write("Error: Undefined measure")
        sys.exit(2)




def measures_arent_compatible():
    sys.stderr.write("Error: Measures aren't compatible")
    sys.exit(2)


def wrong_number(expression: str):
    spaces = [i for i in range(len(expression)) if expression[i] == ' ']
    for space in spaces:
        if space != 0 and space != len(expression)-1 and expression[:space].replace(" ", "")[-1].isdigit() and expression[space+1:].replace(" ", "")[0].isdigit():
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
        if space != 0 and space != len(expression)-1 and expression[space+1:].replace(" ", "")[0].isdigit() and (expression[:space].replace(" ", "")[-1] == '-' or expression[:space].replace(" ", "")[-1] == '+') and (expression[:space].replace(" ", "")[-2] == '-' or expression[:space].replace(" ", "")[-2] == '+'):
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
        if " ." in expression or ". " in expression:
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
    expression = expression.replace(" ", "")
    points = [i for i in range(len(expression)) if expression[i] == '.']
    for i in range(len(points)-1):
        if expression[points[i]+1:points[i+1]].isdigit():
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
        if points[i] == 0:
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
        if points[i] == len(expression)-1:
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)
        if (not expression[points[i]-1].isdigit()) or (not expression[points[i]+1].isdigit()):
            sys.stderr.write("Error: Wrong number")
            sys.exit(2)


def missing_bracket(expression:str):
    if expression.count("(") != expression.count(")"):
        sys.stderr.write("Error: Missing bracket")
        sys.exit(2)

def calculator_validation(expression: str):
    null_expression(expression)
    unknown_symbol(expression)
    binary_operator(expression)
    missing_operand(expression)
    division_by_zero(expression)
    wrong_number(expression)
    missing_bracket(expression)


def converter_velidation(from_measure: str, to_measure:str, measures: list):
    undefined_measure(from_measure, to_measure, measures)
