def feed_children(children, cookies):
    cookies.sort()
    result = 0
    for child in children:
        for i, cook in enumerate(cookies):
            if cook >= child:
                result += 1
                cookies.pop(i)
                break
    print(result)


def main():
    n = input()
    children = [int(x) for x in input().split()]
    m = input()
    cookies = [int(x) for x in input().split()]
    feed_children(children, cookies)


if __name__ == '__main__':
    main()
