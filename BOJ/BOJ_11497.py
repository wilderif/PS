# BOJ_11497
# 통나무 건너뛰기

import sys


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        h = list(map(int, sys.stdin.readline().split()))
        h.sort(reverse=True)
        out = 0
        for i in range(n - 2):
            if h[i] - h[i + 2] > out:
                out = h[i] - h[i + 2]
        print(out)


if __name__ == "__main__":
    solution()
