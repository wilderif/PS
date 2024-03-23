# BOJ_15652
# N과 M (4)

import sys


def backtracking(idx, arr):
    if idx == m:
        print(*arr)
        return None
    else:
        start = 1
        if idx != 0:
            start = arr[idx - 1]
        for i in range(start, n + 1):
            arr[idx] = i
            backtracking(idx + 1, arr)


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(m)]
    backtracking(0, arr)


if __name__ == "__main__":
    main()
