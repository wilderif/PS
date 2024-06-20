# BOJ_10282
# 해킹

import sys
import heapq

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n, d, c = map(int, inp().split())
        graph = [[] for _ in range(n + 1)]
        vis = [float('inf') for _ in range(n + 1)]
        vis[c] = 0
        for _ in range(d):
            a, b, s = map(int, inp().split())
            graph[b].append((a, s))
        min_heap = [(0, c)]
        while min_heap:
            cur_c, cur_v = heapq.heappop(min_heap)
            for nxt_v, nxt_c in graph[cur_v]:
                if vis[nxt_v] > cur_c + nxt_c:
                    vis[nxt_v] = cur_c + nxt_c
                    heapq.heappush(min_heap, (cur_c + nxt_c, nxt_v))
        res1 = 0
        res2 = 0
        for i in range(n + 1):
            if vis[i] != float('inf'):
                res1 += 1
                res2 = max(res2, vis[i])
        print(res1, res2)
        

if __name__ == "__main__":
    main()
