# BOJ_1244
# 스위치 켜고 끄기

import sys


def solution():
    n = int(input())
    arr = [-1] + list(map(int, sys.stdin.readline().split())) + [-1]
    m = int(input())

    while m:
        m -= 1
        a, b = map(int, sys.stdin.readline().split())
        if a == 1:
            idx = 1
            while 1:
                if b * idx > n:
                    break
                arr[b * idx] = (arr[b * idx] + 1) % 2
                idx += 1
        else:
            arr[b] = (arr[b] + 1) % 2
            for i in range(1, n):
                if arr[b - i] == arr[b + i]:
                    arr[b - i] = (arr[b - i] + 1) % 2
                    arr[b + i] = (arr[b + i] + 1) % 2
                else:
                    break

    for i in range(1, n + 1):
        print(arr[i], end=' ')
        if i % 20 == 0:
            print()
    

if __name__ == "__main__":
    solution()
