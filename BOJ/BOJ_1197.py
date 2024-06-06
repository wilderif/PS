# BOJ_1197
# 최소 스패닝 트리

import sys
import heapq

inp = sys.stdin.readline


def main():
    v, e = map(int ,inp().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, inp().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    used = set()
    min_heap = []
    used.add(1)
    for e in graph[1]:
        heapq.heappush(min_heap, e)

    res = 0
    while True:
        cost, nxt = heapq.heappop(min_heap)
        if nxt in used:
            continue
        used.add(nxt)
        res += cost
        for e in graph[nxt]:
            if e[1] not in used:
                heapq.heappush(min_heap, e)
        if len(used) == v:
            break
    print(res)


if __name__ == "__main__":
    main()
