# BOJ_1193
# 분수찾기

import sys


def main():
    x = int(input())
    sec = 1
    p = 1
    cur = 1
    while True:
        if cur >= x:
            x = sec - (cur - x)
            break
        else:
            p += 1
            cur += p
        sec += 1
    if sec % 2:
        print('/'.join([str(sec + 1 - x), str(x)]))
    else:
        print('/'.join([str(x), str(sec + 1 - x)]))


if __name__ == "__main__":
    main()
