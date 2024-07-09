# BOJ_5972
# 택배 배송

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    min_heap = [(0, 1)]
    dist = [float('inf') for _ in range(n + 1)]
    dist[1] = 0

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue

        for nxt_v, nxt_c in graph[cur_v]:
            cost = nxt_c + cur_c
            if cost < dist[nxt_v]:
                dist[nxt_v] = cost
                heapq.heappush(min_heap, (cost, nxt_v))
    
    print(dist[n])

                
if __name__ == "__main__":
    main()
