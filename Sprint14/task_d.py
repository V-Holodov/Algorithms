def feed_children(children, cookies):
    children.sort(reverse=True)
    cookies.sort(reverse=True)
    result = 0
    cook = 0
    for i in range(len(children)):
        if children[i] <= cookies[cook]:
            result += 1
            cook += 1
            if cook >= len(cookies):
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
