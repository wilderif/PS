# BOJ_2479
# 경로 찾기

import sys
from collections import deque

inp = sys.stdin.readline


def check_distance(n1, n2):
    dist = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            dist += 1
        if dist > 1:
            return False

    if dist == 1:
        return True
    return False


def bfs(graph, src, dst):
    q = deque()
    prev = [-1 for _ in range(len(graph))]

    q.append(src)
    prev[src] = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if prev[nxt] != -1:
                continue

            q.append(nxt)
            prev[nxt] = cur

            if nxt == dst:
                break

    if prev[dst] == -1:
        return [-1]

    cur_node = dst
    path = deque()
    while cur_node:
        path.appendleft(cur_node)
        cur_node = prev[cur_node]

    return path


def main():
    n, k = map(int, inp().split())
    arr = [None] + [inp().strip() for _ in range(n)]
    src, dst = map(int, inp().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if check_distance(arr[i], arr[j]):
                graph[i].append(j)
                graph[j].append(i)

    print(*bfs(graph, src, dst))


if __name__ == "__main__":
    main()
