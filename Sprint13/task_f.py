class StackMax():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        print(max(self.items, default='None'))


def metod_stackmax(stackmax, command):
    key = command.split()
    if key[0] == 'push':
        return stackmax.push(int(key[1]))
    elif key[0] == 'pop':
        return stackmax.pop()
    elif key[0] == 'get_max':
        return stackmax.get_max()


if __name__ == '__main__':
    stackmax = StackMax()
    n = int(input())
    for i in range(n):
        metod_stackmax(stackmax, input())
