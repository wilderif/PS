# BOJ_1764
# 듣보잡

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    h_s = set()
    s_s = set()

    for _ in range(n):
        h_s.add(sys.stdin.readline().rstrip())
    for _ in range(m):
        s_s.add(sys.stdin.readline().rstrip())

    out = list(h_s.intersection(s_s))
    out.sort()

    print(len(out))
    for i in out:
        print(i)


if __name__ == "__main__":
    solution()
