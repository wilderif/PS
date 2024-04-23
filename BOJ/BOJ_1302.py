# BOJ_1302
# 베스트셀러

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    d = {}
    for _ in range(n):
        s = inp().rstrip()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    d_list = list(d.items())
    d_list.sort(key=lambda x:(-x[1], x[0]))
    print(d_list[0][0])


if __name__ == "__main__":
    main()
