# BOJ_10974
# 모든 순열

import sys

inp = sys.stdin.readline


def back(depth):
    if depth == n:
        print(*out)
        return
    for i in range(n):
        if not vis[i]:
            vis[i] = True
            out[depth] = i + 1
            back(depth + 1)
            vis[i] = False


def main():
    global n, vis, out
    n = int(inp())
    vis = [False for _ in range(n)]
    out = [0 for _ in range(n)]
    back(0)


if __name__ == "__main__":
    main()
