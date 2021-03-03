def first_digit(nums):
    key = [x for x in nums]
    if len(key) < 4:
        for _ in range(4 - len(key)):
            key.append(key[-1])
    return key


def main():
    n = int(input())
    nums = input().split()
    result = sorted(nums, key=first_digit, reverse=True)
    print(''.join(result))


if __name__ == '__main__':
    main()
