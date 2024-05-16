# BOJ_2660
# 회장뽑기

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [[] for _ in range(n + 1)]
    while True:
        a, b = map(int, inp().split())
        if a == -1 and b == -1:
            break
        graph[a].append(b)
        graph[b].append(a)

    res = [100 for _ in range(n + 1)]
    res_point = 100
    for i in range(1, n + 1):
        vis = [True for _ in range(n + 1)]
        q = deque()
        q.append((i, 0))
        vis[i] = False
        while q:
            cur = q.popleft()
            for nxt in graph[cur[0]]:
                if vis[nxt]:
                    q.append((nxt, cur[1] + 1))
                    vis[nxt] = False
                    res[i] = cur[1] + 1
        res_point = min(res_point, res[i])
    
    res_out = []
    for i in range(1, n + 1):
        if res[i] == res_point:
            res_out.append(i)
    print(res_point, len(res_out))
    print(*res_out)
        
    
if __name__ == "__main__":
    main()
