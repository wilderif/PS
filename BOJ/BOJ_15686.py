# BOJ_15686
# 치킨 배달

import sys

inp = sys.stdin.readline


def check():
    global res
    total_min = 0
    for h in home_arr:
        cur_min = float("inf")
        for i in used:
            c = chicken_arr[i]
            cur_min = min(cur_min, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        total_min += cur_min
    res = min(res, total_min)


def backtracking(start, depth):
    if depth == m:
        check()
        return

    for i in range(start, len(chicken_arr)):
        used.append(i)
        backtracking(i + 1, depth + 1)
        used.pop()


def main():
    global m, home_arr, chicken_arr, res, used
    n, m = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(n)]

    home_arr = []
    chicken_arr = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                home_arr.append((i, j))
            if board[i][j] == 2:
                chicken_arr.append((i, j))

    res = float("inf")
    used = []

    backtracking(0, 0)
    print(res)


if __name__ == "__main__":
    main()
