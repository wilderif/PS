# BOJ_2580
# 스도쿠

import sys

inp = sys.stdin.readline


def check_square(coord, num):
    start = ((coord[0] // 3) * 3, (coord[1] // 3) * 3)
    for i in range(3):
        for j in range(3):
            if board[start[0] + i][start[1] + j] == num:
                return False
    return True


def check_line(coord, num):
    for i in range(9):
        if board[coord[0]][i] == num or board[i][coord[1]] == num:
            return False
    return True


def back(idx):
    if idx == len(check):
        for line in board:
            print(*line)
        sys.exit(0)
    
    for i in range(1, 10):
        if check_square(check[idx], i) and check_line(check[idx], i):
            board[check[idx][0]][check[idx][1]] = i
            back(idx + 1)
            board[check[idx][0]][check[idx][1]] = 0


def main():
    global board, check
    board = [list(map(int, inp().split())) for _ in range(9)]
    check = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                check.append((i, j))
    back(0)


if __name__ == "__main__":
    main()
