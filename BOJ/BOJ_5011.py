# BOJ_5011
# Robots on a grid

import sys
import itertools

inp = sys.stdin.readline


def main():
    MOD = 2**31 - 1
    n = int(inp())
    board = [list(inp().rstrip()) for _ in range(n)]

    def dfs():
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vis = [[False for _ in range(n)] for _ in range(n)]
        vis[0][0] = True
        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if board[nx][ny] == "#":
                    continue
                if vis[nx][ny]:
                    continue
                if nx == n - 1 and ny == n - 1:
                    return True
                vis[nx][ny] = True
                stack.append((nx, ny))
        return False

    def count_path():
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            if board[0][i] == "#":
                break
            dp[0][i] = 1
        for i in range(n):
            if board[i][0] == "#":
                break
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] == "#":
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                dp[i][j] %= MOD
        return dp[-1][-1]

    can_go = dfs()
    if can_go is False:
        print("INCONCEIVABLE")
        return

    path = count_path()
    if path == 0:
        print("THE GAME IS A LIE")
        return
    print(path)


if __name__ == "__main__":
    main()
