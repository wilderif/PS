# BOJ_26168
# 배열 전체 탐색하기

import sys
import bisect

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = sorted(list(map(int, inp().split())))
    for _ in range(m):
        q = list(map(int, inp().split()))
        if q[0] == 1:
            l_b = bisect.bisect_left(arr, q[1])
            print(n - l_b)
        elif q[0] == 2:
            u_b = bisect.bisect_right(arr, q[1])
            print(n - u_b)
        elif q[0] == 3:
            l_b = bisect.bisect_left(arr, q[1])
            u_b = bisect.bisect_right(arr, q[2])
            print(u_b - l_b)


if __name__ == "__main__":
    main()
