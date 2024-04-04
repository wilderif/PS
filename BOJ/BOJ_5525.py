# BOJ_5525
# IOIOI

import sys


def main():
    n = int(input())
    m = int(input())
    s = sys.stdin.readline().rstrip()
    cur, res = 0, 0
    idx = 0
    while idx < m - 2:
        if s[idx:idx + 3] == "IOI":
            cur += 1
            idx += 2
        else:
            if cur >= n:
                res += cur - n + 1
            idx += 1
            cur = 0
    if cur >= n:
        res += cur - n + 1
    print(res)


if __name__ == "__main__":
    main()
