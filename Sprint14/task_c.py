def check_subseq(seq1, seq2):
    n = 0
    start = 0
    while n != len(seq1):
        val = seq1[n]
        try:
            start = seq2.index(val, start)
            n += 1
        except ValueError:
            return False
    return True


def main():
    s = input()
    t = input()
    print(check_subseq(s, t))


if __name__ == '__main__':
    main()
