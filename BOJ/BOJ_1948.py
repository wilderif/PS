# BOJ_1948
# 임계경로

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((b, c))
        indeg[b] += 1
    start, end = map(int, inp().split())
    
    dist = [0 for _ in range(n + 1)]
    stack = [start]
    dist[start] = 0
    passed = [[] for _ in range(n + 1)]
    while stack:
        cur = stack.pop()
        for v, c in graph[cur]:
            if dist[v] < dist[cur] + c:
                dist[v] = dist[cur] + c
                passed[v] = [cur]
            elif dist[v] == dist[cur] + c:
                passed[v].append(cur)
            indeg[v] -= 1
            if not indeg[v]:
                stack.append(v)
    
    res = 0
    stack = []
    used = [False for _ in range(n + 1)]
    for i in passed[end]:
        stack.append(i)
        res += 1
        used[i] = True
    while stack:
        cur = stack.pop()
        for i in passed[cur]:
            res += 1
            if used[i]:
                continue
            stack.append(i)
            used[i] = True

    print(dist[end])
    print(res)
    

if __name__ == "__main__":
    main()
