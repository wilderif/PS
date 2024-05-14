# BOJ_1485
# 정사각형

import sys


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        dot = []
        line_len = []
        for _ in range(4):
            dot.append(list(map(int, sys.stdin.readline().split())))
        for i in range(3):
            for j in range(i + 1, 4):
                line_len.append((dot[i][0] - dot[j][0]) * (dot[i][0] - dot[j][0])
                                + (dot[i][1] - dot[j][1]) * (dot[i][1] - dot[j][1]))
        line_len.sort()
        if line_len[0] == line_len[1] == line_len[2] == line_len[3] and line_len[4] == line_len[5]:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()
