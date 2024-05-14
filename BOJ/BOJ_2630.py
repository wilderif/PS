# BOJ_2630
# 색종이 만들기

import sys


def divide(x, y, size, arr):
    global res_w, res_b
    color = arr[y][x]
    for j in range(y, y + size):
        for i in range(x, x + size):
            if arr[j][i] != color:
                divide(x, y, size // 2, arr)
                divide(x + size // 2, y, size// 2 ,arr)
                divide(x, y + size // 2, size // 2, arr)
                divide(x + size // 2, y + size // 2, size // 2, arr)
                return None
    else:
        if color:
            res_b += 1
        else:
            res_w += 1


def solution():
    n = int(input())
    arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    global res_w, res_b
    res_w, res_b = 0, 0
    divide(0, 0, n, arr)
    print(res_w)
    print(res_b)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
