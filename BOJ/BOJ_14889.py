# BOJ_14889
# 스타트와 링크

import sys

inp = sys.stdin.readline


def check():
    global res
    tmp = 0
    for i in vis:
        tmp += board_row[i]
        tmp += board_col[i]
    res = min(res, abs(tmp - (total - tmp)) // 2)


def backtracking(start):
    if len(vis) == n // 2:
        check()
        return
    for i in range(start, n):
        vis.append(i)
        backtracking(i + 1)
        vis.pop()


def main():
    global n, board_row, board_col, vis, total, res
    n = int(inp())
    board = [list(map(int, inp().split())) for _ in range(n)]
    board_row = [sum(i) for i in board]
    board_col = []
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += board[j][i]
        board_col.append(tmp)
    total = sum(board_row) * 2
    vis = []
    res = float('inf')
    backtracking(0)
    print(res)
            

if __name__ == "__main__":
    main()