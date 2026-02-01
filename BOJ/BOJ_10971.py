# BOJ_10971
# 외판원 순회 2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [list(map(int, inp().split())) for _ in range(n)]
    dp = [[float("inf") for _ in range((1 << n))] for _ in range(n)]
    vis_all = (1 << n) - 1

    def dfs(cur, vis):
        if dp[cur][vis] != float("inf"):
            return dp[cur][vis]

        if vis == vis_all:
            if graph[cur][0] == 0:
                return float("inf")
            dp[cur][vis] = graph[cur][0]
            return dp[cur][vis]

        for nxt in range(n):
            if vis & (1 << nxt):
                continue
            if graph[cur][nxt] == 0:
                continue

            dp[cur][vis] = min(
                dp[cur][vis], dfs(nxt, vis | (1 << nxt)) + graph[cur][nxt]
            )

        return dp[cur][vis]

    print(dfs(0, (1 << 0)))


if __name__ == "__main__":
    main()
