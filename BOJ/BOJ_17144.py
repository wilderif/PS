# BOJ_17144
# 미세먼지 안녕!

import sys


def spread(arr, next):
    for j in range(r):
        for i in range(c):
            if arr[j][i] > 0:
                next[j][i] += arr[j][i]
                tmp = arr[j][i] // 5
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        next[nx][ny] += tmp
                        next[j][i] -= tmp


def clean(next, cleaner):
    for i in range(cleaner[0], 0, -1):
        next[i][0] = next[i - 1][0]
    for i in range(cleaner[1], r - 1):
        next[i][0] = next[i + 1][0]
    next[cleaner[0]][0] = 0
    next[cleaner[1]][0] = 0

    for i in range(c - 1):
        next[0][i] = next[0][i + 1]
        next[r - 1][i] = next[r - 1][i + 1]

    for i in range(cleaner[0]):
        next[i][c - 1] = next[i + 1][c - 1]
    for i in range(r - 1, cleaner[1], -1):
        next[i][c - 1] = next[i - 1][c - 1]

    for i in range(c - 1, 0, -1):
        next[cleaner[0]][i] = next[cleaner[0]][i - 1]
        next[cleaner[1]][i] = next[cleaner[1]][i - 1]


def main():
    global dx, dy, r, c
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    r, c, t = map(int, sys.stdin.readline().split())
    arr = list()
    cleaner = list()
    for i in range(r):
        arr.append(list(map(int, sys.stdin.readline().split())))
        if arr[i][0] == -1:
            cleaner.append(i)
    
    for _ in range(t):
        next = [[0 for _ in range(c)] for _ in range(r)]
        spread(arr, next)
        clean(next, cleaner)
        arr = next

    print(sum(sum(i) for i in arr))
    

if __name__ == "__main__":
    main()
