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
    split_list:list = []
    expression = expression.replace(' ', '')
    for i in range(len(expression)):
        if expression[i] == "(" and i > 1:
            if split_list[-1] == "-" and split_list[-2][-1] != ")" and (not split_list[-2][-1].isdigit()):
                split_list[-1] = "-1"
                split_list.append("*")
                split_list.append("(")
            elif split_list[-1] == "+":
                split_list[-1] = "("
            else:
                split_list.append("(")
        elif expression[i] == "+" and i > 0:
            if split_list[-1] == "-" and split_list[-2][-1] != ")" and (not split_list[-2][-1].isdigit()):
                split_list[-1] = "-"
            elif split_list[-1] == "+":
                split_list[-1] = "+"
            else:
                split_list.append("+")
        elif expression[i] == "-" and i > 0:
            if split_list[-1] == "-":
                split_list[-1] = "+"
            elif split_list[-1] == "+":
                split_list[-1] = "-"
            else:
                split_list.append("-")
        elif (not expression[i].isdigit() and expression[i] != "/" and expression[i] != ".") or i == 0:
            split_list.append(expression[i])
        elif expression[i].isdigit():
            if i >= 2:
                if expression[i - 1].isdigit() or expression[i-1] == "." or ((split_list[-1] == '+' or split_list[-1] == '-') and split_list[-2][-1] != ')' and not split_list[-2][-1].isdigit()):
                    split_list[-1] += expression[i]
                else:
                    split_list.append(expression[i])
            elif i == 1:
                if expression[i - 1].isdigit() or split_list[-1] == '+' or split_list[-1] == '-':
                    split_list[-1] += expression[i]
                else:
                    split_list.append(expression[i])
        elif expression[i] == "/" and i > 0:
            if split_list[-1] == "/":
                split_list[-1] += expression[i]
            else:
                split_list.append(expression[i])
        elif expression[i] == "/":
            split_list.append(expression[i])
        elif expression[i] == ".":
            split_list[-1] += expression[i]
    return split_list


def set_priority(split_list: list[str]):
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

def tokenize(expression: str) -> str:
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
            result += tokenize("".join(split_list[i+1:close_bracket_index]))
            i = close_bracket_index
        elif split_list[i] == "(":
            close_bracket_index = find_close(split_list, i)
            result += tokenize("".join(split_list[i+1:close_bracket_index]))+split_list[i-1]+" "
            i = close_bracket_index
        i += 1
    return result
