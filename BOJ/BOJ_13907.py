# BOJ_13907
# 세금

import sys
import math
import heapq

inp = sys.stdin.readline


def main():
    n, m, k = map(int, inp().split())
    s, d = map(int, inp().split())
    graph = [dict() for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, inp().split())
        if b not in graph[a] or graph[a][b] > w:
            graph[a][b] = w
            graph[b][a] = w
    tax = [0] + [int(inp()) for _ in range(k)]

    dist = [[math.inf for _ in range(n + 1)] for _ in range(n)]
    min_heap = [(0, s, 0)]
    dist[0][s] = 0

    while min_heap:
        cur_c, cur_v, passed = heapq.heappop(min_heap)
        flag = False
        for i in range(passed):
            if dist[i][cur_v] < cur_c:
                flag = True
        if cur_c != dist[passed][cur_v] or passed == n - 1 or cur_v == d or flag:
            continue

        for nxt_v, nxt_c in graph[cur_v].items():
            if dist[passed + 1][nxt_v] > cur_c + nxt_c:
                dist[passed + 1][nxt_v] = cur_c + nxt_c
                heapq.heappush(min_heap, (cur_c + nxt_c, nxt_v, passed + 1))

    path = []
    for i in range(1, n):
        if dist[i][d] != math.inf:
            path.append([i, dist[i][d]])

    for i in range(k + 1):
        res = math.inf
        for j in range(len(path)):
            path[j][1] += tax[i] * path[j][0]
            if res > path[j][1]:
                res = path[j][1]
        print(res)


if __name__ == "__main__":
    main()
