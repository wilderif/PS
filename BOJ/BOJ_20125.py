# BOJ_20125
# 쿠키의 신체 측정

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    board = [inp().strip() for _ in range(n)]
    point = None
    res = [0 for _ in range(5)]

    for i in range(1, n):
        for j in range(1, n):
            if board[i][j] == '*':
                if board[i - 1][j] == '*' and board[i + 1][j] == '*' and \
                      board[i][j - 1] == '*' and board[i][j + 1] == '*':
                    point = (i, j)
                    break
        if point:
            break
    
    tmp_point = [point[0], point[1] - 1]
    while tmp_point[1] >= 0 and board[tmp_point[0]][tmp_point[1]] == '*':
        tmp_point[1] -= 1
        res[0] += 1

    tmp_point = [point[0], point[1] + 1]
    while tmp_point[1] < n and board[tmp_point[0]][tmp_point[1]] == '*':
        tmp_point[1] += 1
        res[1] += 1

    tmp_point = [point[0] + 1, point[1]]
    point_2 = None
    while board[tmp_point[0]][tmp_point[1]] == '*':
        tmp_point[0] += 1
        res[2] += 1
        point_2 = (tmp_point[0], tmp_point[1])
    
    tmp_point = [point_2[0], point_2[1] - 1]
    while tmp_point[0] < n and board[tmp_point[0]][tmp_point[1]] == '*':
        tmp_point[0] += 1
        res[3] += 1
    
    tmp_point = [point_2[0], point_2[1] + 1]
    while tmp_point[0] < n and board[tmp_point[0]][tmp_point[1]] == '*':
        tmp_point[0] += 1
        res[4] += 1

    print(point[0] + 1, point[1] + 1)
    print(*res)


if __name__ == "__main__":
    main()
