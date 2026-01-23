# BOJ_18979
# Triangle Partition

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = sorted(
            [(i + 1, tuple(map(int, inp().split()))) for i in range(n * 3)],
            key=lambda x: x[1][0],
        )

        for i in range(n):
            print(arr[i * 3][0], arr[i * 3 + 1][0], arr[i * 3 + 2][0])


if __name__ == "__main__":
    main()
