# BOJ_15666
# N과 M (12)

import sys

inp = sys.stdin.readline


def backtracking(start, depth):
    if depth == m:
        print(*out)
        return
    last = -1
    for i in range(start, n):
        if arr[i] != last:
            out.append(arr[i])
            backtracking(i, depth + 1)
            out.pop()
            last = arr[i]


def main():
    global n, m, arr, vis, out
    n, m = map(int, inp().split())
    arr = list(map(int, inp().split()))
    arr.sort()
    out = []
    backtracking(0, 0)
    

if __name__ == "__main__":
    main()
