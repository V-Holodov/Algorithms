# ID 48805803

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, value: int) -> None:
        self.items.append(value)

    def pop(self) -> int:
        return self.items.pop()


def comp(a: int, b: int, sign: str) -> int:
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
        }
    return operations[sign](a, b)


def polish_calc(order: list) -> int:
    """Калькулятор с обратной польской нотацией."""
    stack = Stack()
    signs = ('+', '-', '*', '/')
    for value in order:
        if value in signs:
            b = stack.pop()
            a = stack.pop()
            result = comp(a, b, value)
            stack.push(result)
        else:
            stack.push(int(value))
    return stack.pop()


def main() -> None:
    order = input().split()
    print(polish_calc(order))


if __name__ == '__main__':
    main()
