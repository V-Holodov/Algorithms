def comb(seq, item, comand, n, keybord, cursor):
    if n == 0:
        seq = seq + item + ' '
    else:
        for i in keybord[comand[cursor]]:
            comb(seq, item + i, comand, n - 1, keybord, cursor + 1)
    return seq


def main():
    keybord = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
    comand = input()
    print(comb('', '', comand, len(comand), keybord, 0))


if __name__ == '__main__':
    main()
