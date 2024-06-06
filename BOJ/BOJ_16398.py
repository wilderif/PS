# BOJ_16398
# 행성 연결

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [list(map(int, inp().split())) for _ in range(n)]
    
    min_heap = []
    used = set()
    used.add(0)
    for i in range(n):
        heapq.heappush(min_heap, (graph[0][i], i))
    
    res = 0
    while len(used) < n:
        cost, nxt = heapq.heappop(min_heap)
        if nxt in used:
            continue
        res += cost
        used.add(nxt)
        for i in range(n):
            if i in used:
                continue
            heapq.heappush(min_heap, (graph[nxt][i], i))
    print(res)


if __name__ == "__main__":
    main()
