# BOJ_10974
# 모든 순열

import sys

inp = sys.stdin.readline


def backtracking(depth):
    if depth == n:
        print(*out)
        return
    for i in range(n):
        if not vis[i]:
            vis[i] = True
            out.append(i + 1)
            backtracking(depth + 1)
            vis[i] = False
            out.pop()


def main():
    global n, vis, out
    n = int(inp())
    vis = [False for _ in range(n)]
    out = []
    backtracking(0)

                
if __name__ == "__main__":
    main()
