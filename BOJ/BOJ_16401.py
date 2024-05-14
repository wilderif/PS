# BOJ_16401
# 과자 나눠주기

import sys
sys.setrecursionlimit(35000)

inp = sys.stdin.readline


def check(target):
    ret = 0
    for i in snack:
        ret += i // target
    return ret


def search(start, end):
    if start >= end:
        return start
    mid = (start + end + 1) // 2
    if check(mid) < m:
        return search(start, mid - 1)
    else:
        return search(mid, end)


def main():
    global m, n, snack
    m, n = map(int, inp().split())
    snack = list(map(int, inp().split()))
    print(search(0, max(snack)))


if __name__ == "__main__":
    main()
