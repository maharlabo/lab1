import sys

def is_number(number_string: str) -> bool:
    return number_string.isdigit() or ((number_string[0] == '+' or number_string[0] == '-') and number_string[1:].isdigit()) or "." in number_string



def calculate(tokenized_expression: str) -> float:
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
            elif operation == '//':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1//number2)
            elif operation == '/':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1/number2)
            elif operation == '%':
                if number2 == 0:
                    sys.stderr.write("Error: Division by zero")
                    sys.exit(2)
                stack.append(number1%number2)
    return stack[0]
