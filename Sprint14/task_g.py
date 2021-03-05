def sort_cloth(seq):
    arr0 = []
    arr1 = []
    arr2 = []
    for val in seq:
        if val == '0':
            arr0.append(val)
        elif val == '1':
            arr1.append(val)
        if val == '2':
            arr2.append(val)
    result = arr0 + arr1 + arr2
    print(' '.join(result))


def main():
    n = input()
    seq = input()
    sort_cloth(seq)


if __name__ == '__main__':
    main()
