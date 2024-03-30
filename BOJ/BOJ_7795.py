# BOJ_7795
# 먹을 것인가 먹힐 것인가

import sys


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        arr_1 = list(map(int, sys.stdin.readline().split()))
        arr_2 = list(map(int, sys.stdin.readline().split()))
        arr_1.sort(reverse=True)
        arr_2.sort(reverse=True)
        res = 0
        cur = m
        idx1, idx2 = 0, 0
        while idx1 < n and idx2 < m:
            if arr_1[idx1] > arr_2[idx2]:
                res += cur
                idx1 += 1
            else:
                idx2 += 1
                cur -= 1
        print(res)

    
if __name__ == "__main__":
    main()
