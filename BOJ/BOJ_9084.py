# BOJ_9084
# 동전

import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        k = int(sys.stdin.readline())
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
