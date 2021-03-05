def merge(arr: list, left: int, mid: int, right: int) -> list:
    result = arr[:left] + [0] * (right - left + 1) + arr[right + 1:]
    l = k = left
    r = mid + 1
    while l <= mid and r <= right:
        if arr[l] <= arr[r]:
            result[k] = arr[l]
            l += 1
        else:
            result[k] = arr[r]
            r += 1
        k += 1
    while l <= mid:
        result[k] = arr[l]
        l += 1
        k += 1
    while r <= right:
        result[k] = arr[r]
        r += 1
        k += 1
    return result


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left == 1 or right - left == 2:
        arr[:] = merge(arr, left, (right - left) // 2 + left - 1, right - 1)
        return None
    mid = (right - left) // 2 + left
    merge_sort(arr, left, mid)
    left_part = arr
    merge_sort(arr, mid, right)
    right_part = arr
    two_parts = left_part[:mid] + right_part[mid:]
    arr[:] = merge(two_parts, left, mid - 1, right - 1)
    return None


arr = [4, 5, 8, 1, 4, 9, 6, 4, 7, 1, 5]
print(arr)
merge_sort(arr, 2, 9)
print(arr)
