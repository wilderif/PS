# BOJ_2637
# 장난감 조립

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    res = [0 for _ in range(n)] + [1]
    
    for _ in range(m):
        a, b, c = list(map(int, inp().split()))
        graph[a].append((b, c))
        indeg[b] += 1
    
    stack = []
    for i in range(1, n + 1):
        if not indeg[i]:
            stack.append(i)

    while stack:
        cur = stack.pop()
        for v, c in graph[cur]:
            indeg[v] -= 1
            if not indeg[v]:
                stack.append(v)
            res[v] += c * res[cur]
    
    for i in range(1, n):
        if not len(graph[i]):
            print(i, res[i])


if __name__ == "__main__":
    main()
