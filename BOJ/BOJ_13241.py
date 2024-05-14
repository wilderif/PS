# BOJ_13241
# 최소공배수

import sys


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def main():
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))


if __name__ == "__main__":
    main()
