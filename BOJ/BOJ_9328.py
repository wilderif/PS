# BOJ_9328
# 열쇠

import sys

inp = sys.stdin.readline


def initial(c, cor):
    global res, arr
    if c == '.':
        return True
    if c == '$':
        arr[cor[0]][cor[1]] = '.'
        res += 1
        return True
    if c.isalpha():
        if c.islower():
            arr[cor[0]][cor[1]] = '.'
            key.add(c)
        return True
    return False


def dfs(initial_stack):
    global arr, res
    vis = [[True for _ in range(w)] for _ in range(h)]
    stack = list(initial_stack)
    while stack:
        print(stack)
        for i in arr:
            print(*i)
        print()
        cur = stack.pop()
        if arr[cur[0]][cur[1]].isalpha() and arr[cur[0]][cur[1]].isupper():
            if arr[cur[0]][cur[1]].lower() not in key:
                continue
            else:
                arr[cur[0]][cur[1]] = '.'
        if vis[cur[0]][cur[1]]:
            vis[cur[0]][cur[1]] = False
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < h and 0 <= ny < w and vis[nx][ny]:
                if arr[nx][ny] == '.':
                    vis[nx][ny] = False
                    stack.append((nx, ny))
                if arr[nx][ny].isalpha():
                    if arr[nx][ny].islower():
                        key.add(arr[nx][ny])
                        arr[nx][ny] = '.'
                        vis = [[True for _ in range(w)] for _ in range(h)]
                        stack = list(initial_stack)
                        stack.append((nx, ny))
                    else:
                        if arr[nx][ny].lower() in key:
                            arr[nx][ny] = '.'
                            vis[nx][ny] = False
                            stack.append((nx, ny))
                if arr[nx][ny] == '$':
                    res += 1
                    arr[nx][ny] = '.'
                    vis[nx][ny] = False
                    stack.append((nx, ny))
    

def main():
    t = int(inp())
    for _ in range(t):
        global h, w, arr, key, dx, dy, res
        res = 0
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)

        h, w = map(int, inp().split())
        arr = [list(inp().rstrip()) for _ in range(h)]
        key = set()
        tmp = inp().rstrip()
        if tmp == '0':
            pass
        else:
            for k in tmp:
                key.add(k)

        initial_stack = []
        for i in range(w):
            if initial(arr[0][i], (0, i)):
                initial_stack.append((0, i))
            if initial(arr[h - 1][i], (h - 1, i)):
                initial_stack.append((h - 1, i))
        for i in range(h):
            if initial(arr[i][0], (i, 0)):
                initial_stack.append((i, 0))
            if initial(arr[i][w - 1], (i, w - 1)):
                initial_stack.append((i, w - 1))
        dfs(initial_stack)
        print(res)


if __name__ == "__main__":
    main()
