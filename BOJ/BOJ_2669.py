# BOJ_2669
# 직사각형 네개의 합집합의 면적 구하기

import sys


def solution():
    arr = [[False for _ in range(101)] for _  in range(101)]

    for _ in range(4):
        a, b, c, d = map(int, sys.stdin.readline().split())
        for j in range(b, d):
            for i in range(a, c):
                if not arr[j][i]:
                    arr[j][i] = True
    
    res = 0
    for j in range(1, 101):
        for i in range(1, 101):
            if arr[j][i]:
                res += 1
    print(res)


if __name__ == "__main__":
    solution()
