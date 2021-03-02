def bracketGenerator(seq, item, n2, n, tag, open):
    if n2 == 0:
        seq.append(item)
    else:
        if tag != 0:
            bracketGenerator(seq, item + ')', n2-1, n, tag - 1, open)
        if open < n:
            bracketGenerator(seq, item + '(', n2-1, n, tag + 1, open + 1)
    return seq


def main():
    n = int(input())
    n2 = n * 2
    seq = sorted(bracketGenerator([], '', n2, n, 0, 0))
    for i in range(len(seq)):
        print(seq[i])


if __name__ == '__main__':
    main()
