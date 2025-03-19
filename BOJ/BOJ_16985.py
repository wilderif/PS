# BOJ_16985
# Maaaaaaaaaze

import sys
import itertools

inp = sys.stdin.readline


def rotate(board, rotate_cnt):
    ret = [[0 for _ in range(5)] for _ in range(5)]

    if rotate_cnt == 0:
        for i in range(5):
            for j in range(5):
                ret[i][j] = board[i][j]
    elif rotate_cnt == 1:
        for i in range(5):
            for j in range(5):
                ret[i][j] = board[4 - j][i]
    elif rotate_cnt == 2:
        for i in range(5):
            for j in range(5):
                ret[i][j] = board[4 - i][4 - j]
    else:
        for i in range(5):
            for j in range(5):
                ret[i][j] = board[j][4 - i]

    return ret


def search(board_arr):
    if not board_arr[0][0][0] or not board_arr[4][4][4]:
        return False

    dx = (-1, 1, 0, 0, 0, 0)
    dy = (0, 0, -1, 1, 0, 0)
    dz = (0, 0, 0, 0, -1, 1)

    vis = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    cnt = 0
    queue = [(0, 0, 0)]
    vis[0][0][0] = True

    while queue:
        new_queue = []
        cnt += 1
        if cnt > res:
            return False
        for x, y, z in queue:
            for d in range(6):
                nx = x + dx[d]
                ny = y + dy[d]
                nz = z + dz[d]
                if not (0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5):
                    continue
                if not board_arr[nx][ny][nz]:
                    continue
                if vis[nx][ny][nz]:
                    continue
                if nx == 4 and ny == 4 and nz == 4:
                    return cnt
                new_queue.append((nx, ny, nz))
                vis[nx][ny][nz] = True
        queue = new_queue

    return False


def check(board_order, rotate_order):
    global res
    tmp_board_arr = []

    for i in range(5):
        tmp_board_arr.append(board_rotate_arr[board_order[i]][rotate_order[i]])

    return search(tmp_board_arr)


def main():
    global board_rotate_arr, res
    board_arr = []
    for _ in range(5):
        board_arr.append([list(map(int, inp().split())) for _ in range(5)])

    board_rotate_arr = [[] for _ in range(5)]
    for i in range(5):
        for c in range(4):
            board_rotate_arr[i].append(rotate(board_arr[i], c))

    res = float("inf")
    board_order_arr = list(itertools.permutations(range(5), 5))
    rotate_order_arr = list(itertools.product(range(4), repeat=5))

    for i in board_order_arr:
        for j in rotate_order_arr:
            tmp = check(i, j)
            if tmp:
                res = min(res, tmp)
            if res == 12:
                print(res)
                return

    if res == float("inf"):
        print(-1)
        return
    print(res)


if __name__ == "__main__":
    main()
