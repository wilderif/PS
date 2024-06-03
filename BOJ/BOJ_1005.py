# BOJ_1005
# ACM Craft

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n, k = map(int, inp().split())
        cost = [None] + list(map(int, inp().split()))
        graph = [[] for _ in range(n + 1)]
        indeg = [0 for _ in range(n + 1)]
        for _ in range(k):
            a, b = map(int, inp().split())
            graph[a].append(b)
            indeg[b] += 1
        w = int(inp())

        stack = []
        mem = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if not indeg[i]:
                stack.append(i)
            mem[i] = cost[i]

        while stack:
            cur = stack.pop()
            if cur == w:
                print(mem[cur])
                break
            for v in graph[cur]:
                indeg[v] -= 1
                if not indeg[v]:
                    stack.append(v)
                mem[v] = max(mem[v], mem[cur] + cost[v])


if __name__ == "__main__":
    main()
