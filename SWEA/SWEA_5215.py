# SWEA_5215
# 햄버거 다이어트


def solution():
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [0 for _ in range(l + 1)]
    for value, weight in arr:
        for i in range(l, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    return max(dp)


def main():
    t = int(input())
    for i in range(t):
        res = solution()
        print(f"#{i + 1} {res}")


main()
