# BOJ_1766
# 문제집

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    min_heap = []
    res = []

    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
        indeg[b] += 1
    
    for i in range(1, n + 1):
        if not indeg[i]:
            heapq.heappush(min_heap, i)
    
    while min_heap:
        cur = heapq.heappop(min_heap)
        res.append(cur)
        for v in graph[cur]:
            indeg[v] -= 1
            if not indeg[v]:
                heapq.heappush(min_heap, v)
    
    print(*res)


if __name__ == "__main__":
    main()
