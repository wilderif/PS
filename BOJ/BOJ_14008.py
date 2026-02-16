# BOJ_14008
# Medium Weird Measurements

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            dp[i] = 1
            continue

        if i < 2:
            dp[i] = 2
            continue

        tmp_1 = arr[i - 1] - arr[i - 2]
        tmp_2 = arr[i] - arr[i - 1]
        if tmp_1 * tmp_2 < 0:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 2

    print(sum(dp))


if __name__ == "__main__":
    main()
