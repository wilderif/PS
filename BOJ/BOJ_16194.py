# BOJ_16194
# 카드 구매하기 2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [0] + list(map(int, inp().split()))
    mem = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        mem[i] = arr[i]
        tmp = 1000 * 10000
        for j in range(i):
            tmp = min(tmp, mem[j] + mem[i - j])
        mem[i] = tmp
    print(mem[n])
 

if __name__ == "__main__":
    main()
