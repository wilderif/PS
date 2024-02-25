# BOJ_28132
# 기벡을 안배운다고?

import sys
import math


def solution():
    n = int(sys.stdin.readline())
    cnt = dict()
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if x < 0:
            x *= -1
            y *= -1
        elif x == 0 and y < 0:
            y *= -1
        tmp = math.gcd(x, y)
        if tmp:
            x = int(x / tmp)
            y = int(y / tmp)
        if (x, y) in cnt:
            cnt[(x, y)] += 1
        else:
            cnt[(x, y)] = 1
    res = 0
    if (0, 0) in cnt:
        if cnt[(0, 0)] > 1:
            res += int(cnt[(0, 0)] * (cnt[(0, 0)] - 1) / 2)
        res += cnt[(0, 0)] * (n - cnt[(0, 0)])
    for k in cnt.keys():
        if k == (0, 0):
            continue
        else:
            if (k[1], -k[0]) in cnt.keys():
                res += cnt[k] * cnt[(k[1], -k[0])]

    print(res)


if __name__ == "__main__":
    solution()
