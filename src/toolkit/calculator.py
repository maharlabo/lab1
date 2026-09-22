import sys
from toolkit.errors import null_expression
from toolkit.errors import unknown_symbol
from toolkit.errors import binary_operator
from toolkit.errors import missing_operand
from toolkit.errors import division_by_zero
from toolkit.errors import wrong_number
from toolkit.errors import missing_bracket

def validation(expression: str):
    null_expression(expression)
    unknown_symbol(expression)
    binary_operator(expression)
    missing_operand(expression)
    division_by_zero(expression)
    wrong_number(expression)
    missing_bracket(expression)




def find_close(array: list, open_bracket_index: int) -> int:
    count_brackets = 0
    for i in range(open_bracket_index+1, len(array)):
        if array[i] == "(":
            count_brackets += 1
        elif array[i] == ")":
            if count_brackets > 0:
                count_brackets -= 1
            else:
                return i
    return 0

def is_number(number_string: str) -> bool:
    return number_string.isdigit() or ((number_string[0] == '+' or number_string[0] == '-') and number_string[1:].isdigit()) or "." in number_string

def split_expression(expression: str) -> list:
    split_list = []
    expression = expression.replace(' ', '')
    for i in range(len(expression)):
        if not expression[i].isdigit() or i == 0:
            split_list.append(expression[i])
        elif expression[i] == "/" and i > 0:
            if expression[i - 1] == "/":
                split_list[-1] += expression[i]
            else:
                split_list.append(expression[i])
        elif expression[i] == ".":
            split_list[-1] += expression[i]
        elif expression[i].isdigit():
            if i >= 2:
                if expression[i - 1].isdigit() or (
                        (expression[i - 1] == '+' or expression[i - 1] == '-') and not expression[i - 2].isdigit()):
                    split_list[-1] += expression[i]
                else:
                    split_list.append(expression[i])
            elif i == 1:
                if expression[i - 1].isdigit() or expression[i - 1] == '+' or expression[i - 1] == '-':
                    split_list[-1] += expression[i]
                else:
                    split_list.append(expression[i])
    return split_list


def set_priority(split_list: list):
    first_priority_operations = ['*', '/', '//', '%']

    i = 0
    while i < len(split_list):
        if is_number(split_list[i]) and i == 0 and i != len(split_list) - 1 and split_list[
            i + 1] in first_priority_operations:
            i += 1
            while i < len(split_list) and split_list[i] in first_priority_operations:
                i += 2
                if i < len(split_list):
                    if split_list[i - 1] == '(':
                        close_bracket_index = find_close(split_list, i - 1)
                        i = close_bracket_index + 1
        elif is_number(split_list[i]) and i != 0 and i != len(split_list) - 1 and split_list[
            i + 1] in first_priority_operations:
            split_list.insert(i, '(')
            i += 1
            # i += 1
            i += 1
            while i < len(split_list) and split_list[i] in first_priority_operations:
                i += 2
                if i < len(split_list):
                    if split_list[i - 1] == '(':
                        close_bracket_index = find_close(split_list, i - 1)
                        i = close_bracket_index + 1
            split_list.insert(i, ')')
        elif split_list[i] == "(":
            close_bracket_index = find_close(split_list, i)
            i = close_bracket_index
        i += 1

def tokenization(expression: str) -> str:
    split_list = split_expression(expression)
    set_priority(split_list)

    result = ""
    i = 0
    while i < len(split_list):
        if is_number(split_list[i]) and i == 0:
            result += split_list[i]+" "
        elif is_number(split_list[i]):
            result += split_list[i]+" "+split_list[i-1]+" "
        elif split_list[i] == "(" and i == 0:
            close_bracket_index = find_close(split_list, i)
            result += tokenization("".join(split_list[i+1:close_bracket_index]))
            i = close_bracket_index
        elif split_list[i] == "(":
            close_bracket_index = find_close(split_list, i)
            result += tokenization("".join(split_list[i+1:close_bracket_index]))+split_list[i-1]+" "
            i = close_bracket_index
        i += 1

    return result

def calculation(tokenized_expression: str) -> float:
    operations = tokenized_expression.split()
    stack = []
    for operation in operations:
        if is_number(operation):
            stack.append(float(operation[1:]) if operation[0] == '+' else float(operation))
        else:
            number2 = stack.pop()
            number1 = stack.pop()
            if operation == '+':
                stack.append(number1+number2)
            elif operation == '-':
                stack.append(number1-number2)
            elif operation == '*':
                stack.append(number1*number2)
            elif operation == '/':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1/number2)
            elif operation == '//':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1//number2)
            elif operation == '%':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1%number2)
    return stack[0]
