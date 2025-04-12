# BOJ_12896
# 스크루지 민호

import sys

inp = sys.stdin.readline


def bfs(start):
    vis = [False for _ in range(n + 1)]
    ret = 0
    cnt = 0
    q = [start]
    vis[start] = True

    while q:
        nq = []
        cnt += 1
        for cur in q:
            for nxt in tree[cur]:
                if vis[nxt]:
                    continue
                nq.append(nxt)
                vis[nxt] = True
        if nq:
            ret = nq[0]
        q = nq

    return ret, cnt


def main():
    global n, tree

    n = int(inp())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, inp().split())
        tree[u].append(v)
        tree[v].append(u)

    n1, _ = bfs(1)
    _, length = bfs(n1)
    print(length // 2)


if __name__ == "__main__":
    main()
