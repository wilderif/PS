# BOJ_11656
# 접미사 배열

import sys


def solution():
    s = sys.stdin.readline().rstrip()
    arr = []
    for i in range(len(s)):
        arr.append(s[i:])
    arr.sort()
    for i in arr:
        print(i)


if __name__ == "__main__":
    solution()
