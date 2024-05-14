# BOJ_14425
# 문자열 집합

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    
    s = set()
    for _ in range(n):
        s.add(sys.stdin.readline().strip())

    res = 0
    for _ in range(m):
        tmp = sys.stdin.readline().strip()
        if tmp in s:
            res += 1

    print(res)


if __name__ == "__main__":
    solution()
