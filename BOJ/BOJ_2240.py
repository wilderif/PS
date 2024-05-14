# BOJ_2240
# 자두나무

import sys

inp = sys.stdin.readline


def main():
    t, w = map(int, inp().split())
    arr = [int(inp()) for _ in range(t)]
    mem = [[0 for _ in range(w + 1)] for _ in range(t)]
    if arr[0] == 1:
        mem[0][0] += 1
    else:
        mem[0][1] += 1

    for i in range(1, t):
        if arr[i] == 1:
            for j in range(0, min(i + 1, w + 1), 2):
                mem[i][j] = mem[i - 1][j] + 1
            for j in range(1, min(i + 1, w + 1), 2):
                mem[i][j] = mem[i - 1][j]
            for j in range(2, w + 1, 2):
                mem[i][j] = max(mem[i][j], mem[i - 1][j - 1] + 1)
        else:
            for j in range(0, min(i + 1, w + 1), 2):
                mem[i][j] = mem[i - 1][j]
            for j in range(1, min(i + 1, w + 1), 2):
                mem[i][j] = mem[i - 1][j] + 1
            for j in range(1, w + 1, 2):
                mem[i][j] = max(mem[i][j], mem[i - 1][j - 1] + 1)
    print(max(mem[-1]))


if __name__ == "__main__":
    main()
