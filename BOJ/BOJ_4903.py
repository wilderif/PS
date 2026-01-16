# BOJ_4903
# Relax! It’s just a game

import sys

inp = sys.stdin.readline


def main():
    def factorial(num):
        ret = 1
        for i in range(1, num + 1):
            ret *= i
        return ret

    while True:
        a, b = map(int, inp().split())
        if a == -1 and b == -1:
            break
        tmp = factorial(a + b) // factorial(a) // factorial(b)
        if tmp == a + b:
            print(f"{a}+{b}={a+b}")
        else:
            print(f"{a}+{b}!={a+b}")


if __name__ == "__main__":
    main()
