# BOJ_9656
# 돌 게임 2

import sys


def solution():
    n = int(input())
    mem = list(False for _ in range(n + 4))
    mem[2] = True

    for i in range(4, n + 1):
        if not mem[i - 3] or not mem[i - 1]:
            mem[i] = True

    if mem[n]:
        print("SK")
    else:
        print("CY")


if __name__ == "__main__":
    solution()
