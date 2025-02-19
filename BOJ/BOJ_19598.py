# BOJ_19598
# 최소 회의실 개수

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = []
    for _ in range(n):
        s, e = map(int, inp().split())
        arr.append((s, 1))
        arr.append((e, 0))
    arr.sort(key=lambda x: (x[0], x[1]))

    cnt = 0
    res = 0
    for el in arr:
        if el[1]:
            cnt += 1
        else:
            cnt -= 1
        res = max(res, cnt)
    print(res)


if __name__ == "__main__":
    main()
