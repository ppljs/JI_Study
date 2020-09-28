eval_rpn(tokens):
    value_stack = []
    for token in tokens:
        if len(token) > 1 or token.isnumeric():
            value_stack.append(token)
        else:
            right, left = value_stack.pop(), value_stack.pop()
            value_stack.append(calculate(int(left), token, int(right)))

    return value_stack[0]


def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        return int(a / b)
    else:
        return a * b
