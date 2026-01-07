# BOJ_1817
# 짐 챙기는 숌

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    if n == 0:
        print(0)
        return

    arr = list(map(int, inp().split()))
    res = 0
    tmp = 0
    for el in arr:
        if tmp + el > m:
            res += 1
            tmp = el
        else:
            tmp += el
    print(res + 1)


if __name__ == "__main__":
    main()
