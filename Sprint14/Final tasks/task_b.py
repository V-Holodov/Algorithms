def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    while left <= right:
        while arr[left][1] < pivot[1]:
            left += 1
        while arr[right][1] > pivot[1]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr[:right + 1], arr[right + 1:]


def search_median(a, b, c, i):
    s = [a] * 3
    if a[i] < b[i]:
        s[1] = b
    else:
        s[0] = b
    if c[i] >= s[1][i]:
        s[2] = c
    elif c[i] >= s[0][i]:
        s[2], s[1] = s[1], c
    else:
        s[2], s[1], s[0] = s[1], s[0], c
    return s[1]


def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = search_median(arr[0], arr[-1], arr[len(arr) // 2], 1)
    left, right = partition(arr, pivot)
    return qsort(left) + qsort(right)



import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# arr = [randint(0, 10) for i in range(5)]
arr = []
for i in range(5):
    item = (generate_random_string(3), random.randint(0, 10), random.randint(0, 10))
    arr.append(item)
print(arr)
for i in range(len(arr)):
    print(arr[i])

newarr = qsort(arr)
print ('------')
for i in range(len(newarr)):
    print(newarr[i])