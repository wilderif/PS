# BOJ_24230
# 트리 색칠하기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    color = list(map(int, inp().split()))
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, inp().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    res = 1 if color[0] else 0
    stack = [0]
    vis = [True] + [False for _ in range(n - 1)]
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if vis[nxt]:
                continue
            if color[cur] != color[nxt]:
                res += 1
            vis[nxt] = True
            stack.append(nxt)

    print(res)


if __name__ == "__main__":
    main()
