# BOJ_2012
# 등수 매기기

import sys


def solution():
    n = int(sys.stdin.readline())
    exp = []
    out = 0
    for _ in range(n):
        exp.append(int(sys.stdin.readline()))
    exp.sort()
    for i in range(len(exp)):
        if i + 1 - exp[i] > 0:
            out += i + 1 - exp[i]
        else:
            out -= i + 1 - exp[i]
    print(out)


if __name__ == "__main__":
    solution()
