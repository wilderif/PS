# BOJ_1992
# 쿼드트리

import sys


def devide(arr, x, y, size):
    global res
    check_one = True
    check_zero = True
    for j in range(size):
        for i in range(size):
            if arr[x + j][y + i] == '1':
                check_zero = False
            if arr[x + j][y + i] == '0':
                check_one = False
            if not check_one and not check_zero:
                break
        if not check_one and not check_zero:
                break
    if check_one:
        res += "1"
    elif check_zero:
        res += "0"
    else:
        new_size = size // 2
        res += "("
        devide(arr, x, y, new_size)
        devide(arr, x, y + new_size, new_size)
        devide(arr, x + new_size, y, new_size)
        devide(arr, x + new_size, y + new_size, new_size)
        res += ")"


def main():
    global res
    res = ""
    n = int(sys.stdin.readline())
    arr = list()
    for _ in range(n):
        arr.append(sys.stdin.readline().rstrip())
    devide(arr, 0, 0, n)
    print(res)


if __name__ == "__main__":
    main()
