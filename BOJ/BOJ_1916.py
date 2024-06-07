# BOJ_1916
# 최소비용 구하기

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((b, c))
    start, end = map(int, inp().split())
    
    min_heap = [(0, start)]
    dist = [10 ** 9 for _ in range(n + 1)]
    dist[start] = 0

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue
        
        for nxt_v, nxt_c in graph[cur_v]:
            cost = nxt_c + cur_c
            if cost < dist[nxt_v]:
                dist[nxt_v] = cost
                heapq.heappush(min_heap, (cost, nxt_v))

    print(dist[end])


if __name__ == "__main__":
    main()
