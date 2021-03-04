def search_segments(pairs, n):
    pairs.sort()
    result = [pairs.pop(0)]
    for segment in pairs:
        if segment[0] > result[-1][1]:
            result.append(segment)
        elif segment[0] <= result[-1][1] and segment[1] > result[-1][1]:
            result[-1][1] = segment[1]
    return result


def main():
    n = int(input())
    pairs = []
    for _ in range(n):
        pairs.append([int(x) for x in input().split()])
    result = sorted(search_segments(pairs, n))
    for pair in result:
        print(f'{pair[0]} {pair[1]}')


if __name__ == '__main__':
    main()
