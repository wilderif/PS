# BOJ_15665
# N과 M (11)

import sys

inp = sys.stdin.readline


def backtracking(depth):
    if depth == m:
        print(*out)
        return
    last = -1
    for i in range(n):
        if arr[i] != last:
            out.append(arr[i])
            backtracking(depth + 1)
            out.pop()
            last = arr[i]


def main():
    global n, m, arr, vis, out
    n, m = map(int, inp().split())
    arr = list(map(int, inp().split()))
    arr.sort()
    vis = [False for _ in range(n)]
    out = []
    backtracking(0)
    

if __name__ == "__main__":
    main()