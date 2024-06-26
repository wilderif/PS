# BOJ_1388
# 바닥 장식

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    board = [list(inp().rstrip()) for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                res += 1
                if board[i][j] == '-':
                    for k in range(j, m):
                        if board[i][k] == '-':
                            vis[i][k] = True
                        else:
                            break
                else:
                    for k in range(i, n):
                        if board[k][j] == '|':
                            vis[k][j] = True
                        else:
                            break
    print(res)
            

if __name__ == "__main__":
    main()
