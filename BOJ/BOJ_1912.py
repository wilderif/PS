# BOJ_1912
# 연속합

import sys


def solution():
    n = int(input())
    num = list(map(int, sys.stdin.readline().split()))
    mem = [0 for _ in range(n)]
    mem[0] = num[0]
    res = mem[0]
    for i in range(1, n):
        mem[i] = max(mem[i - 1] + num[i], num[i])
        if mem[i] > res:
            res = mem[i]

    print(res)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
