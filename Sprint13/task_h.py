class BracketStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None


def is_correct_bracket_seq(seq):
    bracketstack = BracketStack()
    brackets = {')': '(', ']': '[', '}': '{'}
    for bracket in seq:
        if bracket in brackets.values():
            bracketstack.push(bracket)
        elif bracket in brackets.keys():
            if bracketstack.peek() == brackets[bracket]:
                bracketstack.pop()
            else:
                return False
                break
    return (not bracketstack.items)


if __name__ == '__main__':
    seq = input()
    print(is_correct_bracket_seq(seq))
