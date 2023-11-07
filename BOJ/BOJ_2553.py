# BOJ_2553
# 마지막 팩토리얼 수

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = [1 for _ in range(2)]

    for i in range(2, n + 1):
        arr[0] = arr[1]
        arr[1] = arr[0] * i

    tmp = str(arr[1])
    idx = len(tmp) - 1
    while True:
        if tmp[idx] != '0':
            print(int(tmp[idx]))
            break
        else:
            idx -= 1


if __name__ == "__main__":
    solution()
