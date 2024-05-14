# BOJ_14501
# 퇴사

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [None] + list(list(map(int, inp().split())) for _ in range(n))
    mem = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        mem[i] = max(mem[i - 1], mem[i])
        target = i + arr[i][0] - 1
        if target <= n:
            mem[target] = max(mem[target], mem[i - 1] + arr[i][1])
    print(mem[n])


if __name__ == "__main__":
    main()
