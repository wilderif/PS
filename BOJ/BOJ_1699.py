# BOJ_1699
# 제곱수의 합

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    check = set()
    for i in range(1, int(n ** (1 / 2)) + 1):
        check.add(i ** 2)
    if n in check:
        print(1)
        return
    for i in check:
        if n - i in check:
            print(2)
            return
    for i in check:
        for j in check:
            if n - i - j in check:
                print(3)
                return
    else:
        print(4)
        

if __name__ == "__main__":
    main()
