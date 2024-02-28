# BOJ_1780
# 종이의 개수

import sys


def divide(x, y, size, arr):
    global res_1, res_2, res_3
    num = arr[y][x]
    tmp = size // 3
    for j in range(y, y + size):
        for i in range(x, x + size):
            if arr[j][i] != num:
                divide(x, y, tmp, arr)
                divide(x + tmp, y, tmp, arr)
                divide(x + tmp * 2, y, tmp, arr)
                divide(x, y + tmp, tmp, arr)
                divide(x + tmp, y + tmp, tmp, arr)
                divide(x + tmp * 2, y + tmp, tmp, arr)
                divide(x, y + tmp * 2, tmp, arr)
                divide(x + tmp, y + tmp * 2, tmp, arr)
                divide(x + tmp * 2, y + tmp * 2, tmp, arr)
                return None
    else:
        if num == - 1:
            res_1 += 1
        elif num == 0:
            res_2 += 1
        else:
            res_3 += 1


def solution():
    n = int(input())
    arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    global res_1, res_2, res_3
    res_1, res_2, res_3 = 0, 0, 0
    divide(0, 0, n, arr)
    print(res_1)
    print(res_2)
    print(res_3)


if __name__ == "__main__":
    solution()
