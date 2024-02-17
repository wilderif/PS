# BOJ_9660
# 돌 게임 6

import sys


def solution():
    n = int(input())
    if n % 7 == 2 or n % 7 == 0:
        print("CY")
    else:
        print("SK")


if __name__ == "__main__":
    solution()
