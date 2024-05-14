# BOJ_13913
# 숨바꼭질 4

import sys
from collections import deque


def main():
    n, k = map(int, sys.stdin.readline().split())
    q = deque()
    vis = [[-1, -1] for _ in range(100001)]

    q.append(n)
    vis[n][0] = 0
    vis[n][1] = n

    while (vis[k][0] == -1):
        cur_rocation = q.popleft()
        cur_time = vis[cur_rocation][0]
        for i in [cur_rocation - 1, cur_rocation + 1, cur_rocation * 2]:
            if 0 <= i <= 100000 and vis[i][0] == -1:
                q.append(i)
                vis[i][0] = cur_time + 1
                vis[i][1] = cur_rocation

    res = list()
    res.append(k)
    while True:
        if res[-1] == n:
            break
        res.append(vis[res[-1]][1])

    print(vis[k][0])
    for i in range(len(res) -1, -1, -1):
        print(res[i], end=' ')


if __name__ == "__main__":
    main()
