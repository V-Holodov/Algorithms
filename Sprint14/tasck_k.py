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
    arr = result
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left == 1:
        return merge(arr, left, (right - left) // 2 + left, right)
    merge_sort(arr, left, (right - left) // 2 + left)
    merge_sort(arr, ((right - left) // 2 + left) + 1, right)
    result = merge(arr, left, (right - left) // 2, right)
    return result


print(merge_sort([4, 5, 8, 1, 4, 9, 6, 2, 2, 9, 5], 2, 9))
# print(merge([1, 3, 5, 7, 2, 4, 5, 7, 8], 1, 3, 8))