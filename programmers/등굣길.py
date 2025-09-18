# 등굣길


def solution(m, n, puddles):
    mod = 1_000_000_007
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for y, x in puddles:
        dp[x][y] = -1

    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            dp[i][j] %= mod

    return dp[n][m]
