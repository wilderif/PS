# BOJ_1240
# 노드사이의 거리

import sys
from collections import deque

inp = sys.stdin.readline


def bfs(start, end):
    vis = [10000 * 1000 + 1] * (n + 1)
    q = deque()
    q.append((start, 0))
    vis[start] = True
    while q:
        cur = q.popleft()
        cur_dis = cur[1]
        for e, l in tree[cur[0]]:
            if cur_dis + l < vis[e]:
                vis[e] = cur_dis + l
                q.append((e, cur_dis + l))
    return vis[end]


def main():
    global n, tree
    n, m = map(int, inp().split())
    tree = [[] for _  in range(n + 1)]
    for _ in range(n - 1):
        a, b, l = map(int, inp().split())
        tree[a].append((b, l))
        tree[b].append((a, l))

    for _ in range(m):
        a, b = map(int, inp().split())
        print(bfs(a, b))


if __name__ == "__main__":
    main()
