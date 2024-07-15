# BOJ_2018
# 수들의 합 5

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    res = 0
    p1, p2 = 0, 0
    cur = 0
    while p2 <= n:
        if cur == n:
            res += 1
            cur -= p1
            p1 += 1
        if cur < n:
            p2 += 1
            cur += p2
        else:
            cur -= p1
            p1 += 1
    print(res)


if __name__ == "__main__":
    main()
