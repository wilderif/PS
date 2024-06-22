# BOJ_2805
# 나무 자르기

import sys

inp = sys.stdin.readline


def solve(target):
    tmp = 0
    for i in range(n):
        if arr[i] > target:
            tmp += arr[i] - target
        else:
            break
    return tmp >= m


def b_search():
    start = 0
    end = arr[0]
    while start < end:
        mid = (start + end + 1) // 2
        if solve(mid):
            start = mid
        else:
            end = mid - 1
    return start


def main():
    global n, m, arr
    n, m = map(int, inp().split())
    arr = list(map(int, inp().split()))
    arr.sort(reverse=True)
    print(b_search())


if __name__ == "__main__":
    main()
