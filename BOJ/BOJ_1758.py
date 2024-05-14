# BOJ_1758
# 알바생 강호

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort(reverse=True)
    res = 0
    for i in range(n):
        if arr[i] - i <= 0:
            break
        res += arr[i] - i
    print(res)


if __name__ == "__main__":
    solution()
