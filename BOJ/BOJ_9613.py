# BOJ_9613
# GCD 합

import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        arr = list(map(int, sys.stdin.readline().split()))
        res = 0
        for i in range(1, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                res += gcd(arr[i], arr[j])
        print(res)


if __name__ == "__main__":
    main()
