# BOJ_1980
# 햄버거 사랑

import sys

inp = sys.stdin.readline


def main():
    n, m, t = map(int, inp().split())
    res = 0
    remain = t
    for i in range(t // m + 1):
        tmp_0, tmp_1 = divmod(t - i * m, n)
        if tmp_1 < remain or (tmp_1 == remain and res < tmp_0 + i):
            res = tmp_0 + i
            remain = tmp_1

    print(res, remain)


if __name__ == "__main__":
    main()
