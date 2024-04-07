# BOJ_9465
# 스티커

import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr_1 = list(map(int, sys.stdin.readline().split()))
        arr_2 = list(map(int, sys.stdin.readline().split()))
        mem = [[0 for _ in range(2)] for _ in range(n)]
        mem[0][0] = arr_1[0]
        mem[0][1] = arr_2[0]
        for i in range(1, n):
            if i < 2:
                mem[i][0] = mem[i - 1][1] + arr_1[i]
                mem[i][1] = mem[i - 1][0] + arr_2[i]
            else:
                mem[i][0] = max(mem[i - 1][1], mem[i - 2][1]) + arr_1[i]
                mem[i][1] = max(mem[i - 1][0], mem[i - 2][0]) + arr_2[i]
        print(max(mem[-1]))


if __name__ == "__main__":
    main()
