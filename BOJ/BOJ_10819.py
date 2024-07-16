# BOJ_10819
# 차이를 최대로

import sys

inp = sys.stdin.readline


def check():
    global res
    ret = 0
    for i in range(n - 1):
        ret += abs(out[i] - out[i + 1])
    res = max(res, ret)


def backtracking(depth):
    if depth == n:
        check()
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            out.append(arr[i])
            backtracking(depth + 1)
            used[i] = False
            out.pop()


def main():
    global n, arr, out, used, res
    n = int(inp())
    arr = list(map(int, inp().split()))
    out = []
    used = [False for _ in range(n)]
    res = -100 * n
    backtracking(0)
    print(res)
    

if __name__ == "__main__":
    main()
