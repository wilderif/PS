# BOJ_2225
# 합분해

import sys

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    dp = [[1 for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(2, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            dp[i][j] %= 10**9

    print(dp[k][n])


if __name__ == "__main__":
    main()
