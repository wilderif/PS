# BOJ_18870
# 좌표 압축

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = [[i] for i in range(n)]
    in_arr = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        arr[i].append(in_arr[i])
        arr[i].append(0)

    arr.sort(key=lambda x: x[1])

    for i in range(1, n):
        if arr[i][1] > arr[i - 1][1]:
            arr[i][2] = arr[i - 1][2] + 1
        else:
            arr[i][2] = arr[i - 1][2]

    arr.sort()
    for i in arr:
        print(i[2], end=' ')


if __name__ == "__main__":
    solution()
