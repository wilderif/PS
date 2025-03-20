# BOJ_23059
# 리그 오브 레게노

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = {}
    indeg = {}

    for _ in range(n):
        a, b = inp().split()
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
            indeg[a] = 0

        if b in graph:
            indeg[b] += 1
        else:
            graph[b] = []
            indeg[b] = 1

    res = []
    q = []
    for k, v in indeg.items():
        if v == 0:
            q.append(k)

    while q:
        nq = []
        q.sort()
        for cur in q:
            res.append(cur)
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    nq.append(nxt)
        q = nq

    for v in indeg.values():
        if v >= 1:
            return -1

    return "\n".join(res)


if __name__ == "__main__":
    print(main())
