# BOJ_10165
# 버스 노선

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    arr = []
    for i in range(m):
        a, b = map(int, inp().split())
        if a > b:
            b += n
        else:
            arr.append((a + n, b + n, i + 1))
        arr.append((a, b, i + 1))
    arr.sort(key=lambda x: (x[0], -x[1]))
    res = set([i + 1 for i in range(m)])

    cur_end = 0
    for el in arr:
        if el[1] <= cur_end:
            res.discard(el[2])
        else:
            cur_end = el[1]

    print(*sorted(res))


if __name__ == "__main__":
    main()
