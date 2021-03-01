def binarySearch(s, days, left, right):
    if days[-1] < s:
        return -1
    if right <= left and days[right] >= s:
        return right + 1
    if right <= left:
        return -1
    result = []
    mid = (left + right) // 2
    if mid == 0 and days[0] >= s:
        return 1
    if days[mid-1] < s <= days[mid]:
        return mid + 1
    elif s <= days[mid]:
        return binarySearch(s, days, left, mid)
    elif s > days[mid]:
        return binarySearch(s, days, mid+1, right)


def main():
    n = int(input())
    days = [int(i) for i in input().split()]
    s = int(input())
    day1 = binarySearch(s, days, 0, n-1)
    day2 = binarySearch(s*2, days, 0, n-1)
    print(f'{day1} {day2}')


if __name__ == '__main__':
    main()
