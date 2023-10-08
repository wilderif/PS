# BOJ_10610
# 30

import sys


def solution():
    n = list(sys.stdin.readline().rstrip())

    if '0' not in n:
        print(-1)
    else:
        check = 0
        for i in n:
            check += int(i)
        if check % 3 != 0:
            print(-1)
        else:
            n.sort(reverse=True)
            for i in n:
                print(i, end='')


if __name__ == "__main__":
    solution()
