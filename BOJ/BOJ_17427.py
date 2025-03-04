# BOJ_17427
# 약수의 합 2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    res = 0
    for i in range(1, n + 1):
        res += i * (n // i)
    print(res)


if __name__ == "__main__":
    main()
