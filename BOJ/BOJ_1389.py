# BOJ_1389
# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
        graph[b].append(a)

    res = [n, 100 * 100]
    for i in range(n, 0, -1):
        vis = [-1 for _ in range(n + 1)]
        q = deque()
        q.append(i)
        vis[i] = 0
        while q:
            cur = q.popleft()
            cur_time = vis[cur]
            for e in graph[cur]:
                if vis[e] == -1:
                    vis[e] = cur_time + 1
                    q.append(e)
        if sum(vis) <= res[1]:
            res = [i, sum(vis)]
    print(res[0])


if __name__ == "__main__":
    main()
