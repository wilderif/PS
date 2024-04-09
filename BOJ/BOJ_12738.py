# BOJ_12738
# 가장 긴 증가하는 부분 수열 3

import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    res = [arr[0]]
    for i in arr:
        if res[-1] < i:
            res.append(i)
        elif res[-1] > i:
            res[bisect.bisect_left(res, i)] = i
    print(len(res))


if __name__ == "__main__":
    main()
