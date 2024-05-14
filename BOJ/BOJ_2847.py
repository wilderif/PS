# BOJ_2847
# 게임을 만든 동준이

import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    res = 0
    for i in range(n - 1, 0, -1):
        if arr[i] <= arr[i - 1]:
            res += arr[i - 1] - arr[i] + 1
            arr[i - 1] = arr[i] - 1
    print(res)


if __name__ == "__main__":
    solution()
