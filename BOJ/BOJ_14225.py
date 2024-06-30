# BOJ_14225
# 부분수열의 합

import sys

inp = sys.stdin.readline


def back(start, used_sum):
    check[used_sum] = True
    for i in range(start, n):
        back(i + 1, used_sum + arr[i])


def main():
    global n, arr, used, check
    n = int(inp())
    arr = list(map(int, inp().split()))
    arr.sort()
    used = [False for _ in range(n)]
    check = [False for _ in range(sum(arr) + 2)]
    back(0, 0)

    idx = 0
    while check[idx]:
        idx += 1
    print(idx)


if __name__ == "__main__":
    main()
