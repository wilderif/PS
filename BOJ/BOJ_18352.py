# BOJ_18352
# 특정 거리의 도시 찾기

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n, m, k, x = map(int, inp().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
    vis = [-1 for _ in range(n + 1)]
    q = deque()
    q.append(x)
    vis[x] = 0
    res = set()
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if vis[next] == -1:
                vis[next] = vis[cur] + 1
                q.append(next)
            if vis[next] == k:
                res.add(next)
            if vis[next] > k:
                break
    print(-1 if not res else "\n".join(map(str, sorted(list(res)))))


if __name__ == "__main__":
    main()
