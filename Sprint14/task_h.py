def first_digit(nums):
    key = [x for x in nums]
    if len(key) < 4:
        admix = key[:(4 - len(key))]
        while len(key) != 4:
            for dig in admix:
                key.append(dig)
    return key


def main():
    n = int(input())
    nums = input().split()
    result = sorted(nums, key=first_digit, reverse=True)
    print(''.join(result))


if __name__ == '__main__':
    main()
