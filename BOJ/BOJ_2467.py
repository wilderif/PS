# BOJ_2467
# 용액

import sys
from collections import deque


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    idx_l = 0
    idx_r = n - 1
    res = [arr[idx_l], arr[idx_r]]
    minimum = int(1e9 * 2 + 1)
    while True:
        if idx_l == idx_r:
            break
        cur = arr[idx_l] + arr[idx_r]
        if cur < 0:
            cur = -cur
            if cur < minimum:
                minimum = cur
                res = [arr[idx_l], arr[idx_r]]
            idx_l += 1
        elif cur == 0:
            print(arr[idx_l], end=' ')
            print(arr[idx_r])
            return None
        elif cur > 0:
            if cur < minimum:
                minimum = cur
                res = [arr[idx_l], arr[idx_r]]
            idx_r -= 1

    print(*res)


if __name__ == "__main__":
    main()
