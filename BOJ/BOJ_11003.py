# BOJ_11003
# 최솟값 찾기

import sys
from collections import deque


def main():
    n, l = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    dq = deque()

    for i in range(n):
        tmp = arr[i]
        while dq and dq[-1][1] > tmp:
            dq.pop()   
        dq.append((i, tmp))
        if dq[0][0] <= i - l:
            dq.popleft()
        print(dq[0][1], end=' ')


if __name__ == "__main__":
    main()
