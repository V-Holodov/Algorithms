def commit_intern(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return commit_intern(n-2) + commit_intern(n-1)


def main():
    n = int(input())
    print(commit_intern(n))


if __name__ == '__main__':
    main()
