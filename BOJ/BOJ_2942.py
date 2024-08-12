# BOJ_2942
# 퍼거슨과 사과

import sys

inp = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    r, g = map(int, inp().split())
    gcd_val = gcd(r, g)
    divisor = set()
    for i in range(1, int(gcd_val ** (1 / 2)) + 1):
        if gcd_val % i == 0:
            divisor.add(i)
            divisor.add(gcd_val // i)
    for i in divisor:
        print(i, r // i, g // i)


if __name__ == "__main__":
    main()
