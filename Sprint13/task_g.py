class StackMaxEffective():
    def __init__(self):
        self.items = []
        self.max_item = []

    def push(self, item):
        self.items.append(item)
        if self.max_item:
            if item >= self.max_item[-1]:
                self.max_item.append(item)
        else:
            self.max_item.append(item)

    def pop(self):
        try:
            item = self.items.pop()
            if item == self.max_item[-1]:
                self.max_item.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if self.max_item:
            print(self.max_item[-1])
        else:
            print('None')


def metod_stackmax(stackmax, command):
    key = command.split()
    if key[0] == 'push':
        return stackmax.push(int(key[1]))
    elif key[0] == 'pop':
        return stackmax.pop()
    elif key[0] == 'get_max':
        return stackmax.get_max()


if __name__ == '__main__':
    stackmax = StackMaxEffective()
    n = int(input())
    for i in range(n):
        metod_stackmax(stackmax, input())
