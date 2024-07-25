# BOJ_1080
# 행렬

import sys

inp = sys.stdin.readline


def change(arr, start):
    for i in range(3):
        for j in range(3):
            arr[start[0] + i][start[1] + j] = (arr[start[0] + i][start[1] + j] + 1) % 2


def main():
    n, m = map(int, inp().split())
    arr = [list(map(int, list(inp().rstrip()))) for _ in range(n)]
    target = [list(map(int, list(inp().rstrip()))) for _ in range(n)]

    if n < 3 or m < 3:
        for i in range(n):
            for j in range(m):
                if arr[i][j] != target[i][j]:
                    print(-1)
                    return
        print(0)
        return

    res = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if arr[i][j] != target[i][j]:
                change(arr, (i, j))
                res += 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] != target[i][j]:
                print(-1)
                return
    print(res)
    
        
if __name__ == "__main__":
    main()
