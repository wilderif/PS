# BOJ_11899
# 괄호 끼워넣기

import sys
from collections import deque


def solution():
    s = sys.stdin.readline().rstrip()
    arr = deque()
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(i)

    print(len(arr))


if __name__ == "__main__":
    solution()
