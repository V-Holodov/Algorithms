class MyQueueSized:
    """Очередь на массиве."""
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.current_size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def push(self, value):
        if self.current_size == self.max_size:
            print('error')
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.current_size += 1

    def pop(self):
        if self.is_empty():
            return 'None'
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return 'None'
        return self.queue[self.head]


def get_metod(queue, command):
    key = command.split()
    if key[0] == 'push':
        return queue.push(int(key[1]))
    elif key[0] == 'pop':
        print(queue.pop())
    elif key[0] == 'peek':
        print(queue.peek())
    elif key[0] == 'size':
        print(queue.size())


if __name__ == '__main__':
    n = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for i in range(n):
        get_metod(queue, input())
