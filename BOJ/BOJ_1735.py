# BOJ_1735
# 분수 합

import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    res = [a * d + b * c, b * d]

    gcd = 0
    while True:
        if res[0] > res[1]:
            res[0] %= res[1]
        else:
            res[1] %= res[0]
        if res[0] == 0:
            gcd = res[1]
            break
        if res[1] == 0:
            gcd = res[0]
            break
        
    print((a * d + b * c) // gcd, b * d // gcd)


if __name__ == "__main__":
    main()
