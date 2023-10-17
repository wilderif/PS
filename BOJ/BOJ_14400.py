# BOJ_14400
# 편의점 2

import sys


def solution():
    n = int(sys.stdin.readline())
    x_arr = []
    y_arr = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        x_arr.append(x)
        y_arr.append(y)
    x_arr.sort()
    y_arr.sort()

    # x_med = 0
    # y_med = 0
    # if n % 2 == 1:
    #     x_med = x_arr[n // 2]
    #     y_med = y_arr[n // 2]
    # else:
    #     x_med = (x_arr[n // 2] + x_arr[n // 2 - 1]) / 2
    #     y_med = (y_arr[n // 2] + y_arr[n // 2 - 1]) / 2
    x_med = x_arr[n // 2]
    y_med = y_arr[n // 2]

    res = 0
    for i in range(n):
        res += abs(x_arr[i] - x_med)
        res += abs(y_arr[i] - y_med)
    print(res)


if __name__ == "__main__":
    solution()
