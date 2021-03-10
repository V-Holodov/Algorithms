# ID 49301677


def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr[:right + 1], arr[right + 1:]


def search_median(a, b, c):
    s = [a] * 3
    if a < b:
        s[1] = b
    else:
        s[0] = b
    if c >= s[1]:
        s[2] = c
    elif c >= s[0]:
        s[2], s[1] = s[1], c
    else:
        s[2], s[1], s[0] = s[1], s[0], c
    return s[1]


def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = search_median(arr[0], arr[-1], arr[len(arr) // 2])
    left, right = partition(arr, pivot)
    return qsort(left) + qsort(right)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        item = input().split()
        arr.append([-int(item[1]), int(item[2]), item[0]])
    newarr = qsort(arr)
    for i in range(len(newarr)):
        print(newarr[i][2])


if __name__ == '__main__':
    main()
