# BOJ_11052
# 카드 구매하기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [0] + list(map(int, inp().split()))
    mem = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            mem[j] = max(mem[j], arr[i] + mem[j - i])
    print(mem[-1])


if __name__ == "__main__":
    main()
