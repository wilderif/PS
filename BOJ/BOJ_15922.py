# BOJ_15922
# 아우으 우아으이야!!

import sys


def solution():
    n = int(sys.stdin.readline())
    line_list = list()
    out = 0

    for i in range(n):
        line_list.append(list(map(int, sys.stdin.readline().split())))

    line_list.sort()

    out += line_list[0][1] - line_list[0][0]
    y = line_list[0][1]
    for i in line_list:
        if i[1] <= y:
            continue
        elif i[0] <= y:
            out += i[1] - y
        else:
            out += i[1] - i[0]
        y = i[1]
    print(out)


if __name__ == "__main__":
    solution()
