# BOJ_2293
# 동전 1

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort()
    mem = [0 for _ in range(k + 1)]
    for i in arr:
        if i > k:
            break
        mem[i] += 1
        for j in range(i, k + 1):
            mem[j] += mem[j - i]
    print(mem[k])


if __name__ == "__main__":
    main()
