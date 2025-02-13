# BOJ_7579
# 앱

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    m_arr = [0] + list(map(int, inp().split()))
    c_arr = [0] + list(map(int, inp().split()))
    length = sum(c_arr) + 1

    dp = [[0 for _ in range(length)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        mem = m_arr[i]
        cost = c_arr[i]
        for j in range(length):
            if j < cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + mem)

    for i in range(length):
        if dp[-1][i] >= m:
            print(i)
            return


if __name__ == "__main__":
    main()
