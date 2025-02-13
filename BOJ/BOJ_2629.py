# BOJ_2629
# 양팔저울

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [0] + list(map(int, inp().split()))
    length = sum(arr)

    dp = [False for _ in range(length + 1)]

    for i in range(1, n + 1):
        nxt_dp = dp[:]
        cur = arr[i]
        nxt_dp[cur] = True
        for j in range(length + 1):
            if (
                (0 <= cur - j and dp[cur - j])
                or (0 <= j - cur and dp[j - cur])
                or (j + cur <= length - 1 and dp[j + cur])
            ):
                nxt_dp[j] = True
        dp = nxt_dp

    m = int(inp())
    m_arr = list(map(int, inp().split()))
    for el in m_arr:
        if el > length or not dp[el]:
            print("N", end=" ")
        else:
            print("Y", end=" ")


if __name__ == "__main__":
    main()
