def feed_children(children, cookies):
    cookies.sort()
    children.sort()
    result = 0
    for child in children:
        flag = True
        for cook in cookies:
            if cook >= child:
                result += 1
                cookies.remove[cook]
                flag = False
                break
        if flag:
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
