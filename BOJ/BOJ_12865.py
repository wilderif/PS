# BOJ_12865
# 평범한 배낭

import sys

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    arr = list(tuple(map(int, inp().split())) for _ in range(n))
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weght, value = arr[i - 1]
        for w in range(1, k + 1):
            if w < weght:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weght] + value)

    print(dp[n][k])


if __name__ == "__main__":
    main()
