# BOJ_32403
# 전구 주기 맞추기

import sys

inp = sys.stdin.readline


def main():
    n, t = map(int, inp().split())
    res = 0
    for el in list(map(int, inp().split())):
        cnt = 0
        while True:
            if t % (el + cnt) == 0:
                break
            if el > cnt and t % (el - cnt) == 0:
                break
            cnt += 1
        res += cnt

    print(res)


if __name__ == "__main__":
    main()
