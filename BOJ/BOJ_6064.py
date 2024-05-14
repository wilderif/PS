# BOJ_6064
# 카잉 달력

import sys


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
    

def solve(x, y, m, n):
    tmp = x
    if x == 0:
        tmp += m
    while tmp <= last:
        if tmp % n == y:
            print(tmp)
            break
        tmp += m
    else:
        print(-1)


def main():
    t = int(input())
    for _ in range(t):
        global n, m, last
        m, n, x, y = map(int, sys.stdin.readline().split())
        if x == m:
            x = 0
        if y == n:
            y = 0

        g = gcd(m, n)
        last = m * n // g
        
        if m > n:
            solve(x, y, m, n)
        else:
            solve(y, x, n, m)


if __name__ == "__main__":
    main()
