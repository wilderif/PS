# BOJ_17845
# 수강 과목

import sys

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    arr = [None] + [tuple(map(int, inp().split())) for _ in range(k)]
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        imp, time = arr[i]
        for j in range(n + 1):
            if time > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + imp)

    print(dp[k][n])


if __name__ == "__main__":
    main()
