# BOJ_11399
# ATM

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort(reverse=True)
    res = 0
    for i in range(n):
        res += arr[i] * (i + 1)
    print(res)


if __name__ == "__main__":
    solution()
