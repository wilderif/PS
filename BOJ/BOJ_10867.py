# BOJ_10867
# 중복 빼고 정렬하기

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = set(map(int, sys.stdin.readline().split()))
    arr = sorted(list(arr))
    for i in arr:
        print(i, end=' ')


if __name__ == "__main__":
    solution()
