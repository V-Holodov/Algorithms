class Node:
    """Узел списка."""
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyQueueList:
    """Очередь на связном списке."""
    def __init__(self):
        self.current_size = 0
        self.head = None
        self.tail = None
        self.last_node = None

    def put(self, x):
        if self.head:
            node = Node(x)
            self.last_node.next_item = node
            self.tail = node.next_item
            self.last_node = node
        else:
            self.head = self.last_node = Node(x)
            self.tail = self.head.next_item
        self.current_size += 1

    def get(self):
        if self.head:
            x = self.head.value
            self.head = self.head.next_item
            self.current_size -= 1
            return x
        return 'error'

    def size(self):
        return self.current_size


def get_metod(queue, command):
    key = command.split()
    if key[0] == 'put':
        return queue.put(int(key[1]))
    elif key[0] == 'get':
        print(queue.get())
    elif key[0] == 'size':
        print(queue.size())


if __name__ == '__main__':
    n = int(input())
    queue = MyQueueList()
    for i in range(n):
        get_metod(queue, input())
