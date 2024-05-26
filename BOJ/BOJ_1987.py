# BOJ_1987
# 알파벳

import sys

inp = sys.stdin.readline


def bfs(arr, r, c):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    cur = set()
    cur.add((0, 0, arr[0][0]))
    res = 0
    while cur:
        res += 1
        next = set()
        while cur:
            cur_x, cur_y, cur_str = cur.pop()
            for d in range(4):
                nx = cur_x + dx[d]
                ny = cur_y + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] not in cur_str:
                        next.add((nx, ny, cur_str + arr[nx][ny]))
        cur = next
            
    return res


def main():
    r, c = map(int, inp().split())
    arr = [inp().strip() for _ in range(r)]
    print(bfs(arr, r, c))

    
if __name__ == "__main__":
    main()
