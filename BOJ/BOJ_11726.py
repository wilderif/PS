# BOJ_11726
# 2×n 타일링

import sys


def solution():
    sys.setrecursionlimit(1010)

    def fill(num):
        if mem[num] != -1:
            return mem[num]
        else:
            if num == 0:
                mem[0] = 1
                return mem[num]
            elif num == 1:
                mem[1] = 1
                return mem[num]
            else:
                mem[num] = fill(num - 1) + fill(num - 2)
                return mem[num]

    mem = [-1 for _ in range(1002)]
    n = int(input())

    print(fill(n) % 10007)


if __name__ == "__main__":
    solution()