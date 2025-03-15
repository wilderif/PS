# BOJ_15661
# 링크와 스타트

import sys

inp = sys.stdin.readline


def check():
    global res
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            if vis[i] and vis[j]:
                ret += arr[i][j]
                ret += arr[j][i]
            if not vis[i] and not vis[j]:
                ret -= arr[i][j]
                ret -= arr[j][i]
    res = min(res, abs(ret))


def backtracking(start, depth):
    if start == n:
        check()
        if res == 0:
            print(res)
            sys.exit(0)
        return

    vis[start] = True
    backtracking(start + 1, depth + 1)
    vis[start] = False
    backtracking(start + 1, depth + 1)


def main():
    global n, arr, res, vis
    n = int(inp())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    res = float("inf")
    vis = [False for _ in range(n)]
    vis[0] = True
    backtracking(1, 1)
    print(res)


if __name__ == "__main__":
    main()
