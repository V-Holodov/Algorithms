def bubbleSort(seq, n):
    flag = True
    flag2 = True
    while flag:
        flag = False
        for i in range(n - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                flag = True
                flag2 = False
        if flag or flag2:
            print(' '.join([str(x) for x in seq]))


def main():
    n = int(input())
    seq = [int(x) for x in input().split()]
    bubbleSort(seq, n)


if __name__ == '__main__':
    main()
