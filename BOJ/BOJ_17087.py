# BOJ_17087
# 숨바꼭질 6

import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    n, s = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        if arr[i] - s < 0:
            arr[i] = -(arr[i] - s)
        else:
            arr[i] = arr[i] - s
    cur = arr[0]
    for i in arr:
        cur = gcd(cur, i)
    print(cur)


if __name__ == "__main__":
    main()
