# BOJ_14728
# 벼락치기

import sys

inp = sys.stdin.readline


def main():
    n, t = map(int, inp().split())
    arr = [None] + [tuple(map(int, inp().split())) for _ in range(n)]
    dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        k, s = arr[i]
        for j in range(t + 1):
            if k > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - k] + s)

    print(dp[n][t])


if __name__ == "__main__":
    main()
