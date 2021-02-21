def transpose_matrix(n, m, list_str):
    """
    Транспонирует матрицу.

    Принимает количество строк, столбцев и матрицу в виде списка списков.
    """

    for column_matrix in range(m):
        l = []
        for str_matrix in range(n):
            l.append(list_str[str_matrix][column_matrix])
        print(' '.join(l))


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    list_str = []
    for i in range(n):
        list_str.append(input().split())
    transpose_matrix()
