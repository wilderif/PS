# BOJ_1516
# 게임 개발

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    cost = [0 for _ in range(n + 1)]
    for i in range(n):
        tmp = list(map(int, inp().split()))
        cost[i + 1] = tmp[0]
        for j in range(1, len(tmp) - 1):
            graph[tmp[j]].append(i + 1)
            indeg[i + 1] += 1
    
    q = deque()
    res = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not indeg[i]:
            q.append(i)
            res[i] = cost[i]

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            res[nxt] = max(res[nxt], res[cur] + cost[nxt])
            if not indeg[nxt]:
                q.append(nxt)
    
    for i in range(1, n + 1):
        print(res[i])


if __name__ == "__main__":
    main()
