# BOJ_9789
# Friendship Graph

import sys

inp = sys.stdin.readline


def main():
    input_data = map(int, sys.stdin.read().split())

    def dfs(start):
        vis = [False for _ in range(v)]
        vis[start] = True
        stack = [start]

        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if vis[nxt]:
                    continue
                vis[nxt] = True
                stack.append(nxt)

        return vis

    v, e = next(input_data), next(input_data)
    graph = [set() for _ in range(v)]
    for i in range(v):
        graph[i].add(i)
    for _ in range(e):
        a, b = next(input_data), next(input_data)
        graph[a].add(b)

    reach = []
    for i in range(v):
        reach.append(dfs(i))

    q = next(input_data)
    for _ in range(q):
        x, y = next(input_data), next(input_data)
        print(int(reach[x][y]))


if __name__ == "__main__":
    main()
