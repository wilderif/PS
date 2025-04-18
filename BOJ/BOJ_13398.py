# BOJ_13398
# 연속합 2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = arr[0]
    dp[1][0] = arr[0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

    return max(max(dp[0]), max(dp[1]))


if __name__ == "__main__":
    print(main())
