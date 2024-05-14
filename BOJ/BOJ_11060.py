# BOJ_11060
# 점프 점프

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    vis = [-1 for _ in range(n)]
    q = deque()
    q.append(0)
    vis[0] = 0
    while q:
        cur = q.popleft()
        cur_time = vis[cur]
        for i in range(arr[cur] + 1):
            next = cur + i
            if next >= n:
                break
            if vis[next] == -1 or vis[next] > cur_time + 1:
                vis[next] = cur_time + 1
                q.append(next)
        if vis[-1] != -1:
            print(vis[-1])
            return
    print(-1)            


if __name__ == "__main__":
    main()
