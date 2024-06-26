# BOJ_1182
# 부분수열의 합

import sys

inp = sys.stdin.readline


def check():
    tmp = 0
    for i in range(n):
        if vis[i]:
            tmp += arr[i]
    return tmp == s


def backtracking(depth, target, start):
    global res
    if depth == target:
        tmp = check()
        if tmp:
            res += 1
        return
    for i in range(start, n):
        if not vis[i]:
            vis[i] = True
            backtracking(depth + 1, target, i)
            vis[i] = False


def main():
    global n, s, arr, vis, res
    n, s = map(int, inp().split())
    arr = list(map(int, inp().split()))
    vis = [False for _ in range(n)]
    res = 0
    for i in range(1, n + 1):
        backtracking(0, i, 0)
    print(res)


if __name__ == "__main__":
    main()
