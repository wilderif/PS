# BOJ_16953
# A → B

import sys


def solution():
    a, b = map(int, sys.stdin.readline().split())
    cnt = 0
    while a < b:
        if b % 10 == 1:
            b -= 1
            b /= 10
            b = int(b)
            cnt += 1
        elif b % 2 == 0:
            b /= 2
            b = int(b)
            cnt += 1
        else:
            break

    if a == b:
        print(cnt + 1)
    else:
        print(-1)


if __name__ == "__main__":
    solution()
