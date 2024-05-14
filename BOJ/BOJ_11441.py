# BOJ_11441
# 합 구하기

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n):
        arr[i] += arr[i - 1]

    arr = [0] + arr
    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        print(arr[b] - arr[a - 1])


if __name__ == "__main__":
    solution()
