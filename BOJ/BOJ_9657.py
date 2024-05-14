# BOJ_9657
# 돌 게임 3

import sys


def solution():
    n = int(input())
    mem = list(False for _ in range(n + 5))
    mem[1] = mem[3] = mem[4] = True


    for i in range(5, n + 1):
        if not mem[i - 3] or not mem[i - 1] or not mem[i - 4]:
            mem[i] = True

    if mem[n]:
        print("SK")
    else:
        print("CY")


if __name__ == "__main__":
    solution()
