# BOJ_23827
# 수열 (Easy)

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    prefix = [arr[0]]
    for i in range(1, n):
        prefix.append(prefix[i - 1] + arr[i])
        prefix[i] %= 1000000007
    
    res = 0
    for i in range(n):
        res += arr[i] * (prefix[n - 1] - prefix[i])
        res %= 1000000007
    print(res)


if __name__ == "__main__":
    main()
