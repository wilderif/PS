# BOJ_2072
# 오목

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [tuple(map(int, inp().split())) for _ in range(n)]

    board = [[0 for _ in range(19)] for _ in range(19)]

    def check(x, y):
        if (
            check_5(x, y, 1, 0)
            or check_5(x, y, 0, 1)
            or check_5(x, y, 1, 1)
            or check_5(x, y, -1, 1)
        ):
            return True
        return False

    def check_5(x, y, dx, dy):
        cur_color = board[x][y]
        cnt = 1
        nx, ny = x + dx, y + dy
        while 0 <= nx < 19 and 0 <= ny < 19:
            if board[nx][ny] != cur_color:
                break
            cnt += 1
            nx += dx
            ny += dy

        nx, ny = x - dx, y - dy
        while 0 <= nx < 19 and 0 <= ny < 19:
            if board[nx][ny] != cur_color:
                break
            cnt += 1
            nx -= dx
            ny -= dy

        if cnt == 5:
            return True
        return False

    for i in range(n):
        x, y = arr[i]
        x -= 1
        y -= 1
        board[x][y] = 1 if i % 2 else -1
        if check(x, y):
            print(i + 1)
            return

    print(-1)


if __name__ == "__main__":
    main()
