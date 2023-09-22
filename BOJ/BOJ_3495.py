# BOJ_3495
# 아스키 도형

import sys


def solution():
    h, w = map(int, sys.stdin.readline().split())
    count_half = 0
    count_full = 0
    for _ in range(h):
        l = sys.stdin.readline().rstrip()
        check = False
        for i in l:
            if i == '.' and check is True:
                count_full += 1
            elif (i == '/' or i == '\\') and check is True:
                count_half += 1
                check = False
            elif (i == '/' or i == '\\') and check is False:
                count_half += 1
                check = True

    print(count_full + int(count_half / 2))


if __name__ == "__main__":
    solution()
