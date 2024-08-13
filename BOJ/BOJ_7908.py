# BOJ_7908
# Will It Stop?

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    used = set()
    used.add(n)
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 3
        if n in used:
            print("NIE")
            return
        used.add(n)
    print("TAK")


if __name__ == "__main__":
    main()
