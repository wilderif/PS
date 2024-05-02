# BOJ_2302
# 극장 좌석

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    arr = [0] + [int(inp()) for _ in range(m)] + [n + 1]
    if n == m:
        print(1)
        return
    mem = [0 for _ in range(41)]
    mem[0] = 1
    mem[1] = 1
    mem[2] = 2
    for i in range(3, len(mem)):
        mem[i] = mem[i - 1] + mem[i - 2]
    res = 1
    for i in range(1, m + 2):
        res *= mem[arr[i] - arr[i - 1] - 1]
    print(res)


if __name__ == "__main__":
    main()
