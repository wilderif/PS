# BOJ_16236
# 아기 상어

import sys

inp = sys.stdin.readline


def bfs():
    global start, cur_size, eat_cnt, res
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    used = [[False for _ in range(n)] for _ in range(n)]
    queue = [start]
    cnt = 0
    while queue:
        next_queue = []
        can_eat = []
        cnt += 1
        for nxt in queue:
            for d in range(4):
                nx = nxt[0] + dx[d]
                ny = nxt[1] + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if used[nx][ny] or board[nx][ny] > cur_size:
                        continue
                    next_queue.append((nx, ny))
                    used[nx][ny] = True
                    if board[nx][ny] < cur_size and board[nx][ny]:
                        can_eat.append((nx, ny))
        if can_eat:
            can_eat.sort(key=lambda x: (x[0], x[1]))
            start = can_eat[0]
            board[can_eat[0][0]][can_eat[0][1]] = 0
            eat_cnt += 1
            if eat_cnt == cur_size:
                cur_size += 1
                eat_cnt = 0
            res += cnt
            return True
        queue = next_queue
    return False

    
def main():
    global n, cur_size, board, start, eat_cnt, res
    n = int(inp())
    board = [list(map(int, inp().split())) for _ in range(n)]
    cur_size = 2
    eat_cnt = 0
    start = None
    res = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                start = (i, j)
                board[i][j] = 0
    while True:
        flag = bfs()
        if not flag:
            break
    print(res)


if __name__ == "__main__":
    main()
 