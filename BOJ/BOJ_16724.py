# BOJ_16724
# 피리 부는 사나이

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    board = [inp().strip() for _ in range(n)]
    vis = [[True for _ in range(m)] for _ in range(n)]
    direction = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
    res = 0
    for i in range(n):
        for j in range(m):
            if vis[i][j]:
                cycle = set()
                cur = (i, j)
                vis[i][j] = False
                while True:
                    cycle.add(cur)
                    d = board[cur[0]][cur[1]]
                    next = (cur[0] + direction[d][0], cur[1] + direction[d][1])
                    if vis[next[0]][next[1]]:
                        vis[next[0]][next[1]] = False
                        cur = next
                    else:
                        if next in cycle:
                            res += 1
                        break
    print(res)


if __name__ == "__main__":
    main()
