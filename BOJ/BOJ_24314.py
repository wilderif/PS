# BOJ_24314
# 알고리즘 수업 - 점근적 표기 2

import sys

inp = sys.stdin.readline


def main():
    a1, a2 = map(int, inp().split())
    c = int(inp())
    n = int(inp())
    if a1 >= c and a1 * n + a2 >= c * n:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
