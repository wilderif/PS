# BOJ_2170
# 선 긋기

import sys


def solution():
    t = int(sys.stdin.readline())
    draw = []
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        draw.append([a, b])
    draw.sort()

    end = draw[0][1]
    res = draw[0][1] - draw[0][0]
    for i in draw:
        if i[1] <= end:
            continue
        else:
            if i[0] > end:
                res += i[1] - i[0]
                end = i[1]
            else:
                res += i[1] - end
                end = i[1]
    print(res)


if __name__ == "__main__":
    solution()
