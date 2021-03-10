# ID 49324606


class Participant:
    """
    Сведения об участнике контеста.

    Содержит имя - name, количество решенных задач - tasks
    и размер штрафа - penalty.
    При сравнении сначало учитывается количество решенных задач,
    затем штраф, затем лексографически имя.
    """

    def __init__(self, name: str, tasks: int, penalty: int) -> None:
        self.name = name
        self.tasks = tasks
        self.penalty = penalty
        self.place = (-self.tasks, self.penalty, self.name)

    def __lt__(self, other) -> bool:
        return self.place < other.place

    def __gt__(self, other) -> bool:
        return self.place > other.place


def qsort(arr: list[Participant], start: int, end: int) -> list:
    if end - start < 1:
        return arr
    pivot = arr[end]
    left = start
    right = end
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    qsort(arr, start, right)
    qsort(arr, right + 1, end)
    return arr


def main() -> None:
    n = int(input())
    arr = []
    for _ in range(n):
        partic = input().split()
        arr.append(Participant(partic[0], int(partic[1]), int(partic[2])))
    qsort(arr, 0, len(arr) - 1)
    for item in arr:
        print(item.name)


if __name__ == '__main__':
    main()
