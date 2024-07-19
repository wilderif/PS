# BOJ_3135
# 라디오

import sys

inp = sys.stdin.readline


def main():
    a, b = map(int, inp().split())
    res = abs(a - b)
    n = int(inp())
    for _ in range(n):
        tmp = abs(b - int(inp())) + 1
        res = min(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
