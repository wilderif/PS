# BOJ_2644
# 촌수계산

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    a, b = map(int, inp().split())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, inp().split())
        graph[x].append(y)
        graph[y].append(x)
    q = deque()
    vis = [-1 for _ in range(n + 1)]
    q.append(a)
    vis[a] = 0
    while q:
        cur = q.popleft()
        cur_time = vis[cur]
        for e in graph[cur]:
            if e == b:
                print(cur_time + 1)
                return
            if vis[e] == -1:
                vis[e] = cur_time + 1
                q.append(e)
    print(-1)


if __name__ == "__main__":
    main()
