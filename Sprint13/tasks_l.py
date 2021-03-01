def feb(n: int) -> int:
    cursor = 0
    next = 1
    for _ in range(n):
        cursor, next = next, cursor + next
    return next


def mod(number, k):
    return number % (10 ** k)


def main():
    comand = input().split()
    n = int(comand[0])
    k = int(comand[1])
    commits = feb(n)
    print(mod(commits, k))


if __name__ == '__main__':
    main()
