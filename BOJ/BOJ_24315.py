# BOJ_24315
# 알고리즘 수업 - 점근적 표기 3

import sys

inp = sys.stdin.readline


def main():
    a1, a2 = map(int, inp().split())
    c1, c2 = map(int, inp().split())
    n = int(inp())
    if c1 <= a1 <= c2 and a1 * n + a2 >= c1 * n and a1 * n + a2 <= c2 * n:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
