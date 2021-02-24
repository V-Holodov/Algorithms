# ID 48699680

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(int(value))

    def pop(self):
        return self.items.pop()


def comp(a, b, sign):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
        }
    return operations[sign](a, b)


def polish_calc(order):
    """Калькулятор с обратной польской нотацией."""
    stack = Stack()
    signs = ['+', '-', '*', '/']
    for value in order:
        if value in signs:
            b = stack.pop()
            a = stack.pop()
            result = comp(a, b, value)
            stack.push(result)
        else:
            stack.push(value)
    return stack.pop()


if __name__ == '__main__':
    order = input().split()
    print(polish_calc(order))
