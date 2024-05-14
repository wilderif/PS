# BOJ_11292
# 키 큰 사람

import sys


def solution():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break

        res = []
        l_h = 0
        for _ in range(n):
            name, h = sys.stdin.readline().split()
            h = float(h)
            if h > l_h:
                res = [name]
                l_h = h
            elif h == l_h:
                res.append(name)

        for i in res:
            print(i, end=' ')
        print()


if __name__ == "__main__":
    solution()
