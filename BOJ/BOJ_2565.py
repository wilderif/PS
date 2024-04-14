# BOJ_2565
# 전깃줄

import sys
import bisect


def main():
    n = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])
    res = []
    for i in range(n):
        target = arr[i][1]
        if not res or res[-1] < target:
            res.append(arr[i][1])
        else:
            res[bisect.bisect_left(res, target)] = target
    print(n - len(res))


if __name__ == "__main__":
    main()
