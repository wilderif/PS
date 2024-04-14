# BOJ_12789
# 도키도키 간식드리미

import sys
from collections import deque


def main():
    n = int(input())
    arr = deque(map(int, sys.stdin.readline().split()))
    stack = []
    target = 1
    while arr:
        if arr[0] == target:
            arr.popleft()
            target += 1
        else:
            stack.append(arr.popleft())
        while stack:
            if stack[-1] == target:
                stack.pop()
                target += 1
            else:
                break
    if stack:
        print("Sad")
    else:
        print("Nice")


if __name__ == "__main__":
    main()
