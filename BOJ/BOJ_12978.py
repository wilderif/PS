# BOJ_12978
# 스크루지 민호 2

import sys

sys.setrecursionlimit(10**5)

inp = sys.stdin.readline


def dfs(cur_node):
    vis[cur_node] = True

    for nxt_node in tree[cur_node]:
        if vis[nxt_node]:
            continue

        dfs(nxt_node)
        dp[cur_node][0] += dp[nxt_node][1]
        dp[cur_node][1] += min(dp[nxt_node])


def main():
    global tree, vis, dp

    n = int(inp())
    tree = [[] for _ in range(n + 1)]
    vis = [False for _ in range(n + 1)]
    dp = [[0, 1] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, inp().split())
        tree[u].append(v)
        tree[v].append(u)

    dfs(1)

    print(min(dp[1]))


if __name__ == "__main__":
    main()
