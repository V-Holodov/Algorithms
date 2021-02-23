# ID 48669331


def comp(a, b, sign):
    """Выполнение арифметической операции в зависимости от знака операции."""
    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '/':
        result = a // b
    elif sign == '*':
        result = a * b
    return result


def polish_calc(order):
    """Калькулятор с обратной польской нотацией."""
    stack = []
    signs = ['+', '-', '*', '/']
    for value in order:
        if value in signs:
            b = int(stack.pop())
            a = int(stack.pop())
            result = comp(a, b, value)
            stack.append(result)
        else:
            stack.append(value)
    return stack.pop()


if __name__ == '__main__':
    order = input().split()
    print(polish_calc(order))
