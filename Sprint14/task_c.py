def check_subseq(seq1, seq2):
    seq1.sort()
    seq2.sort()
    for idx, val in enumerate(seq1):
        if val != seq2[idx]:
            return False
    return True


def main():
    seq1 = [x for x in input()]
    seq2 = [x for x in input()]
    print(check_subseq(seq1, seq2))


if __name__ == '__main__':
    main()
