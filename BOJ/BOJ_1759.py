# BOJ_1759
# 암호 만들기

import sys


def backtracking(idx, arr, arr_out):
    if idx == l:
        v = 0
        res = ""
        for i in range(l):
            if arr[arr_out[i]] in ('a', 'e', 'i', 'o', 'u'):
                v += 1
            res += arr[arr_out[i]]
        if 1 <= v <= l - 2:
            print(res)
    else:
        start = 0
        if idx:
            start = arr_out[idx - 1] + 1
        for i in range(start, c):
            arr_out[idx] = i
            backtracking(idx + 1, arr, arr_out)


def main():
    global l, c
    l, c = map(int, sys.stdin.readline().split())
    arr = list(sys.stdin.readline().split())
    arr.sort()
    arr_out = [None for _ in range(l)]
    backtracking(0, arr, arr_out)


if __name__ == "__main__":
    main()
