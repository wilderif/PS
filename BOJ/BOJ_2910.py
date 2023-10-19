# BOJ_2910
# 빈도 정렬

import sys


def solution():
    n, c = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    check = {}
    for i in range(n):
        if arr[i] not in check.keys():
            check[arr[i]] = [i, 1]
        else:
            check[arr[i]][1] += 1
    check = list(check.items())
    check.sort(key=lambda x: (-x[1][1], x[1][0]))

    for i in check:
        for j in range(i[1][1]):
            print(i[0], end=' ')


if __name__ == "__main__":
    solution()
