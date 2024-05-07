# BOJ_6118
# 숨바꼭질

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
        graph[b].append(a)
    for e in graph:
        e.sort(reverse=True)
    vis = [[-1, i] for i in range(n + 1)]
    q = deque()
    q.append(1)
    vis[1][0] = 0
    while q:
        cur = q.popleft()
        cur_time = vis[cur][0]
        for e in graph[cur]:
            if vis[e][0] == -1:
                vis[e][0] = cur_time + 1
                q.append(e)
    
    vis.sort(key=lambda x: (-x[0], x[1]))
    res = [0, 0, 0]
    res[0] = vis[0][1]
    res[1] = vis[0][0]
                 
    for i in vis:
        if i[0] == res[1]:
            res[2] += 1
        else:
            break
    print(*res)


if __name__ == "__main__":
    main()
