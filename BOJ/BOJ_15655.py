# BOJ_15655
# N과 M (6)

import sys


def backtracking(idx, arr_out, used, arr):
    if idx == m:
        for i in range(m):
            print(arr[arr_out[i]], end=' ')
        print()
        return None
    else:
        start = 0
        if idx != 0:
            start = arr_out[idx - 1]
        for i in range(start, n):
            if not used[i]:
                arr_out[idx] = i
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
