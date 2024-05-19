# BOJ_14503
# 로봇 청소기

import sys

inp = sys.stdin.readline


def main():
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    n, m = map(int, inp().split())
    robot = list(map(int, inp().split()))
    arr = [list(map(int, inp().split())) for _ in range(n)]

    cnt = 0
    while True:
        if arr[robot[0]][robot[1]] == 0:
            cnt += 1
            arr[robot[0]][robot[1]] = 2
    
        for d in range(4):
            tmp_dir = (robot[2] + 3 - d) % 4
            nx = robot[0] + dx[tmp_dir]
            ny = robot[1] + dy[tmp_dir]
            if arr[nx][ny] == 0:
                robot[0] = nx
                robot[1] = ny
                robot[2] = tmp_dir
                break
        else:
            nx = robot[0] - dx[robot[2]]
            ny = robot[1] - dy[robot[2]]
            if arr[nx][ny] == 1:
                print(cnt)
                return
            else:
                robot[0] = nx
                robot[1] = ny

    
if __name__ == "__main__":
    main()
