# BOJ_1004
# 어린 왕자

import sys

inp = sys.stdin.readline


def is_in_circle(coor1, coor2, r):
    return (coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2 < r ** 2


def main():
    t = int(inp())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, inp().split())
        n = int(inp())
        res = 0
        for _ in range(n):
            cx, cy, r = map(int, inp().split())
            tmp1 = is_in_circle((x1, y1), (cx, cy), r)
            tmp2 = is_in_circle((x2, y2), (cx, cy), r)
            if (tmp1 and tmp2) or (not tmp1 and not tmp2):
                continue
            res += 1
        print(res)
            

if __name__ == "__main__":
    main()
