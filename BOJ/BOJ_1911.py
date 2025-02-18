# BOJ_1911
# 흙길 보수하기

import sys

inp = sys.stdin.readline


def main():
    n, l = map(int, inp().split())
    arr = list(tuple(map(int, inp().split())) for _ in range(n))
    arr.sort(key=lambda x: x[0])

    res = 0
    cur_end = 0

    for el in arr:
        if el[1] <= cur_end:
            continue
        start = max(cur_end, el[0])
        cnt = None
        if (el[1] - start) % l:
            cnt = (el[1] - start) // l + 1
        else:
            cnt = (el[1] - start) // l

        res += cnt
        cur_end = start + l * cnt
    print(res)


if __name__ == "__main__":
    main()
