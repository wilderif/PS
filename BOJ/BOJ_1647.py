# BOJ_1647
# 도시 분할 계획

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [{} for _ in range(n + 1)]
    start = [0, 1000]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if c < start[1]:
            start[0] = a
            start[1] = c
        if b not in graph[a]:
            graph[a][b] = c
            graph[b][a] = c
        else:
            if graph[a][b] > c:
                graph[a][b] = c
                graph[b][a] = c
    used = set()
    min_heap = []
    used.add(start[0])
    for v, c in graph[start[0]].items():
        heapq.heappush(min_heap, (c, v))

    res_cost = []
    while min_heap:
        cost, nxt = heapq.heappop(min_heap)
        if nxt in used:
            continue
        used.add(nxt)
        res_cost.append(cost)
        for v, c in graph[nxt].items():
            if v not in used:
                heapq.heappush(min_heap, (c, v))
        if len(used) == n:
            break
    
    max_cost = 0
    res = 0
    for c in res_cost:
        res += c
        max_cost = max(max_cost, c)
    print(res - max_cost)
    
        
if __name__ == "__main__":
    main()
