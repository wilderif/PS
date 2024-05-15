# BOJ_11559
# Puyo Puyo

import sys

inp = sys.stdin.readline


def pop_candy(arr):
    pop_event = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.':
                continue
            cur_color = arr[i][j]
            to_delelte = []
            stack = []
            vis = [[True for _ in range(6)] for _ in range(12)]
            stack.append((i, j))
            to_delelte.append((i, j))
            vis[i][j] = False
            count = 1
            while stack:
                cur = stack.pop()
                for d in range(4):
                    nx = cur[0] + dx[d]
                    ny = cur[1] + dy[d]
                    if 0 <= nx < 12 and 0 <= ny < 6 and vis[nx][ny]:
                        if arr[nx][ny] == cur_color:
                            stack.append((nx, ny))
                            to_delelte.append((nx, ny))
                            vis[nx][ny] = False
                            count += 1
            if count >= 4:
                for c in to_delelte:
                    arr[c[0]][c[1]] = '.'
                pop_event = True
    return pop_event


def after_pop(arr):
    for i in range(6):
        stack = []
        for j in range(12):
            if arr[j][i] != '.':
                stack.append(arr[j][i])
        for j in range(11, -1, -1):
            if stack:
                arr[j][i] = stack.pop()
            else:
                arr[j][i] = '.'


def main():
    global dx, dy
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    arr = [list(inp().rstrip()) for _ in range(12)]
    
    res = 0
    while True:
        event = pop_candy(arr)
        if not event:
            break
        after_pop(arr)
        res += 1
    print(res)


if __name__ == "__main__":
    main()
