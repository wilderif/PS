# BOJ_2294
# 동전 2

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list()
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()

    mem = list(10001 for _ in range(k + 1))
    for i in arr:
        if i > k:
            break
        mem[i] = 1
        for j in range(i, k + 1):
            mem[j] = min(mem[j], mem[j - i] + 1)

    if mem[k] == 10001:
        print(-1)
    else:
        print(mem[k])


if __name__ == "__main__":
    main()
