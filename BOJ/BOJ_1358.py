# BOJ_1358
# 하키

import sys

inp = sys.stdin.readline


def main():
    w, h, x, y, p = map(int, inp().split())
    r = h // 2
    res = 0
    for _ in range(p):
        a, b = map(int, inp().split())
        a -= x
        b -= y
        if b < 0 or h < b:
            continue
        if 0 <= a <= w and 0 <= b <= h:
            res += 1
        else:
            dist1 = a ** 2 + (b - r) ** 2
            dist2 = (a - w) ** 2 + (b - r) ** 2
            if dist1 <= r ** 2 or dist2 <= r ** 2:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
