# BOJ_1094
# 막대기

import sys

inp = sys.stdin.readline


def main():
    x = int(inp())
    res = 0
    tmp = 1
    while x:
        if tmp * 2 > x:
            x -= tmp
            tmp = 1
            res += 1
        else:
            tmp *= 2

    print(res)


if __name__ == "__main__":
    main()
