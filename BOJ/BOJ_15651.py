# BOJ_15651
# N과 M (3)

import sys


def backtracking(idx, arr):
    if idx == m:
        print(*arr)
        return None
    else:
        for i in range(1, n + 1):
            arr[idx] = i
            backtracking(idx + 1, arr)


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(m)]
    backtracking(0, arr)


if __name__ == "__main__":
    main()
