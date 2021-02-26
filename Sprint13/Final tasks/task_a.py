# ID 48804612
import typing


class MyDeq:
    """Реализация структуры дек на массиве."""
    max_size: int

    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.deq = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def push_back(self, value: str) -> typing.Union[str, None]:
        if self.size == self.max_size:
            return 'error'
        self.deq[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value: str) -> typing.Union[str, None]:
        if self.size == self.max_size:
            return 'error'
        self.head = (self.head - 1) % self.max_size
        self.deq[self.head] = value
        self.size += 1

    def pop_front(self) -> str:
        if self.size == 0:
            return 'error'
        x = self.deq[self.head]
        self.size -= 1
        self.head = (self.head + 1) % self.max_size
        return x

    def pop_back(self) -> str:
        if self.size == 0:
            return 'error'
        x = self.deq[(self.tail - 1) % self.max_size]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x


def get_metod(deq: MyDeq, command: str) -> typing.Union[str, None]:
    """Вызов метода на основе поступившей команды."""
    key = command.split()
    if key[0] == 'push_back':
        return deq.push_back(key[1])
    elif key[0] == 'push_front':
        return deq.push_front(key[1])
    elif key[0] == 'pop_front':
        return deq.pop_front()
    elif key[0] == 'pop_back':
        return deq.pop_back()


def main() -> None:
    n = int(input())
    max_size = int(input())
    deq = MyDeq(max_size)
    for _ in range(n):
        result = get_metod(deq, input())
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
