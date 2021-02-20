# ID 48161792


def nearest_zero(n, street):
    sheme = []
    count = n
    for house in street:
        if house == '0':
            sheme.append(0)
            count = 1
        else:
            sheme.append(count)
            count += 1
    sheme.reverse()
    count = 1
    exist_zero = False
    for i, distance in enumerate(sheme):
        if distance == 0:
            count = 1
            exist_zero = True
        elif count < distance and exist_zero:
            sheme[i] = count
            count += 1
    sheme.reverse()
    sheme = [str(x) for x in sheme]
    return ' '.join(sheme)


if __name__ == '__main__':
    n = int(input())
    street = input().split()
    print(nearest_zero(n, street))
