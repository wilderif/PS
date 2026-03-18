# BOJ_15243
# Tiling

import sys

inp = sys.stdin.readline


def main():
    mod = 1000000007
    w = int(inp())

    if w % 2:
        print(0)
        return

    dp = [0] * max(5, (w + 1))
    dp[0] = 1
    dp[2] = 3
    for i in range(4, w + 1, 2):
        dp[i] = dp[i - 2] * 3 + sum(dp[: i - 3]) * 2
        dp[i] %= mod
    print(dp[w])


if __name__ == "__main__":
    main()
