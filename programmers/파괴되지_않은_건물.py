# 파괴되지_않은_건물


def solution(board, skill):
    n = len(board)
    m = len(board[0])
    prefix_board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        prefix_board[r1][c1] += degree
        prefix_board[r1][c2 + 1] -= degree
        prefix_board[r2 + 1][c1] -= degree
        prefix_board[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(1, m):
            prefix_board[i][j] += prefix_board[i][j - 1]

    for j in range(m):
        for i in range(1, n):
            prefix_board[i][j] += prefix_board[i - 1][j]

    res = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix_board[i][j]
            if board[i][j] > 0:
                res += 1

    return res
