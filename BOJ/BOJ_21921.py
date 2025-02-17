# BOJ_21921
# 블로그

import sys

inp = sys.stdin.readline


def main():
    n, x = map(int, inp().split())
    arr = [0] + list(map(int, inp().split()))
    res = 0
    res_cnt = 0
    cur = 0
    for i in range(x):
        cur += arr[i]
    for i in range(0, n - x + 1):
        cur -= arr[i]
        cur += arr[i + x]
        if cur > res:
            res = cur
            res_cnt = 1
        elif cur == res:
            res_cnt += 1

    if res == 0:
        print("SAD")
        return
    print(res)
    print(res_cnt)


if __name__ == "__main__":
    main()
