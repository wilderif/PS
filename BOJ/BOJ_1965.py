# BOJ_1965
# 상자넣기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    mem = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                mem[i] = max(mem[i], mem[j] + 1)
    print(max(mem))


if __name__ == "__main__":
    main()
