# BOJ_15650
# N과 M (2) 

import sys


def backtracking(idx, arr, used):
    if idx == m:
        print(*arr)
        return None
    else:
        start = 1
        if idx != 0:
            start = arr[idx - 1] + 1
        for i in range(start, n + 1):
            if not used[i]:
                used[i] = True
                arr[idx] = i
                backtracking(idx + 1, arr, used)
                used[i] = False


def main():
    global n, m
    n, m = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(m)]
    used = [False for _ in range(n + 1)]
    backtracking(0, arr, used)


if __name__ == "__main__":
    main()
