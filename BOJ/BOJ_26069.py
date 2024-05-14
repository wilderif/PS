# BOJ_26069
# 붙임성 좋은 총총이

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    s = set()
    s.add("ChongChong")
    for _ in range(n):
        a, b = inp().rstrip().split()
        if a in s or b in s:
            s.add(a)
            s.add(b)
    print(len(s))


if __name__ == "__main__":
    main()
