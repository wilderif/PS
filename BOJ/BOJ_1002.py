# BOJ_1002
# 터렛

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, inp().split())
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        r_sqr = (r1 + r2) ** 2
        if dist == 0:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        else:
            if dist > r_sqr:
                print(0)
            elif dist == r_sqr:
                print(1)
            else:
                r_sqr_2 = (r1 - r2) ** 2
                if dist < r_sqr_2:
                    print(0)
                elif dist == r_sqr_2:
                    print(1)
                else:
                    print(2)


if __name__ == "__main__":
    main()
