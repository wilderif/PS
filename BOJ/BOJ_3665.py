# BOJ_3665
# 최종 순위

import sys

inp = sys.stdin.readline


def solution():
    n = int(inp())
    arr = list(map(int, inp().split()))
    graph = [set() for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[arr[i]].add(arr[j])
            indeg[arr[j]] += 1
    m = int(inp())
    change = [list(map(int, inp().split())) for _ in range(m)]
    for a, b in change:
        if a in graph[b]:
            graph[a].add(b)
            graph[b].remove(a)
            indeg[a] -= 1
            indeg[b] += 1
        elif b in graph[a]:
            graph[b].add(a)
            graph[a].remove(b)
            indeg[b] -= 1
            indeg[a] += 1
        else:
            print("IMPOSSIBLE")
            return
    
    stack = []
    res = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            stack.append(i)
    while stack:
        if len(stack) > 1:
            print("?")
            return
        cur = stack.pop()
        res.append(cur)
        for v in graph[cur]:
            indeg[v] -= 1
            if not indeg[v]:
                stack.append(v)
    if len(res) < n:
        print("IMPOSSIBLE")
        return
    print(*res)


def main():
    t = int(inp())
    for _ in range(t):
        solution()


if __name__ == "__main__":
    main()
