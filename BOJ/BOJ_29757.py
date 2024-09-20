# BOJ_29757
# 트리 긋기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [[i + 1] + list(map(int, inp().split())) for i in range(n)]
    arr.sort(key=lambda x: (x[1], x[2]))
    for i in range(n - 1):
        print(arr[i][0], arr[i + 1][0])


if __name__ == "__main__":
    main()
