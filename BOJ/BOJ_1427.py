# BOJ_1427
# 소트인사이드

import sys


def solution():
    n = list(sys.stdin.readline().rstrip())
    n.sort(reverse=True)
    for i in n:
        print(i, end='')


if __name__ == "__main__":
    solution()
