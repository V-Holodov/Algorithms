# ID 49187387


def binar_search(arr: list, k: int, left: int, right: int) -> int:
    """Бинарный поиск частично осортированного массива."""
    mid = left + (right - left) // 2
    if not arr:
        return -1
    elif right <= left:
        return right if arr[right] == k else -1
    elif arr[mid] == k:
        return mid
    elif arr[left] < arr[mid]:
        if arr[left] <= k < arr[mid]:
            return binar_search(arr, k, left, mid)
        else:
            return binar_search(arr, k, mid + 1, right)
    elif arr[mid] < arr[right]:
        if arr[mid] < k <= arr[right]:
            return binar_search(arr, k, mid + 1, right)
        else:
            return binar_search(arr, k, left, mid)


def main() -> None:
    n = int(input())
    k = int(input())
    arr = [int(x) for x in input().split()]
    print(binar_search(arr, k, 0, n - 1))


if __name__ == '__main__':
    main()
