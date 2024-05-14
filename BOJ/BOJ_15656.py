# BOJ_15656
# N과 M (7)

import sys


def backtracking(idx, arr_out, arr):
    if idx == m:
        print(*arr_out)
        return None
    else:
        for i in range(n):
            arr_out[idx] = arr[i]
            backtracking(idx + 1, arr_out, arr)


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    arr_out = [0 for _ in range(m)]
    backtracking(0, arr_out, arr)


if __name__ == "__main__":
    main()
