# BOJ_30875
# Recovering the Region

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    board = [list(map(int, inp().split())) for _ in range(n)]

    for i in range(n):
        print(f"{i % 2 + 1} " * n)


if __name__ == "__main__":
    main()
