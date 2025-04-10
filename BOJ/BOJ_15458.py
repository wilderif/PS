# BOJ_15458
# Barn Painting

import sys

inp = sys.stdin.readline


def dfs(cur_node):
    vis[cur_node] = True

    for nxt_node in tree[cur_node]:
        if vis[nxt_node]:
            continue

        dfs(nxt_node)

        tmp = sum(dp[nxt_node])
        for i in range(3):
            dp[cur_node][i] *= tmp - dp[nxt_node][i]
            dp[cur_node][i] %= mod


def main():
    global mod, tree, vis, dp
    mod = 10**9 + 7
    n, k = map(int, inp().split())
    tree = [[] for _ in range(n + 1)]
    vis = [False for _ in range(n + 1)]
    dp = [[1 for _ in range(3)] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, inp().split())
        tree[u].append(v)
        tree[v].append(u)

    for _ in range(k):
        b, c = map(int, inp().split())
        for i in range(3):
            if i + 1 == c:
                continue
            dp[b][i] = 0

    dfs(1)

    print(sum(dp[1]) % mod)


if __name__ == "__main__":
    main()
