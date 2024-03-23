# BOJ_15654
# N과 M (5)

import sys


def backtracking(idx, arr_out, used, arr):
    if idx == m:
        print(*arr_out)
        return None
    else:
        for i in range(n):
            if not used[i]:
                arr_out[idx] = arr[i]
                used[i] = True
                backtracking(idx + 1, arr_out, used, arr)
                used[i] = False


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    arr_out = [0 for _ in range(m)]
    used = [False for _ in range(n)]
    backtracking(0, arr_out, used, arr)


if __name__ == "__main__":
    main()
