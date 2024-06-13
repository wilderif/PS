# BOJ_1497
# 기타콘서트

import sys

inp = sys.stdin.readline


def is_all(arr, used):
    tmp = 0
    for i in range(n):
        if used[i]:
            tmp = tmp | arr[i]
    return bin(tmp).count("1")


def backtracking(arr, target, depth, used, start):
    global cur_max, cur_res
    if depth == target:
        cur = is_all(arr, used)
        if cur > cur_max:
            cur_max = cur
            cur_res = target
        return
    for i in range(start, n):
        if not used[i]:
            used[i] = True
            backtracking(arr, target, depth + 1, used, i + 1)
            used[i] = False


def main():
    global n, m, cur_max, cur_res
    n, m = map(int, inp().split())
    arr = []
    for _ in range(n):
        _, tmp = inp().split()
        tmp2 = "".join(['1' if c == 'Y' else '0' for c in tmp])
        arr.append(int(tmp2, 2))

    cur_max = 0
    cur_res = 0
    for i in range(n):
        used = [False for _ in range(n)]
        backtracking(arr, i + 1, 0, used, 0)
    
    if cur_max == 0:
        print(-1)
    else:
        print(cur_res)


if __name__ == "__main__":
    main()
