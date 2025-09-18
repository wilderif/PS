# BOJ_3190
# 뱀

import sys
from collections import deque

inp = sys.stdin.readline


def can_move(board, new_head):
    if not (0 <= new_head[0] < len(board) and 0 <= new_head[1] < len(board)):
        return False
    if board[new_head[0]][new_head[1]] == 2:
        return False


def move(board, snake, dir):
    head = snake[0]
    new_head = None
    if dir == 0:
        new_head = [head[0], head[1] + 1]
    elif dir == 1:
        new_head = [head[0] + 1, head[1]]
    elif dir == 2:
        new_head = [head[0], head[1] - 1]
    elif dir == 3:
        new_head = [head[0] - 1, head[1]]

    if can_move(board, new_head) == False:
        return False

    if board[new_head[0]][new_head[1]] != 1:
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0
    snake.appendleft(new_head)
    board[new_head[0]][new_head[1]] = 2

    return True


def main():
    n = int(inp())
    k = int(inp())
    board = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, inp().split())
        board[a - 1][b - 1] = 1
    l = int(inp())
    inst = deque()
    for _ in range(l):
        a, b = inp().split()
        b = -1 if b == 'L' else 1
        inst.append((int(a), b))

    time = 0
    dir = 0
    board[0][0] = 2
    snake = deque()
    snake.append([0, 0])

    while True:
        time += 1
        done = move(board, snake, dir)
        if not done:
            break
        if (inst and inst[0][0] == time):
            dir = (dir + inst[0][1] + 4) % 4
            inst.popleft()

    print(time)


if __name__ == "__main__":
    main()
