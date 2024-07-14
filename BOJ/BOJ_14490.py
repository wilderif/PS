# BOJ_14490
# 백대열

import sys

inp = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    n, m  = map(int, inp().split(":"))
    tmp = gcd(n, m)
    print(n // tmp, end=':')
    print(m // tmp)


if __name__ == "__main__":
    main()
