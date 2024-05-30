# BOJ_2252
# 줄 세우기

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    stack = []
    res = []
    for _ in range(m):
        a, b = map(int, inp().split())
        indegree[b] += 1
        graph[a].append(b)
    for i in range(1, n + 1):
        if not indegree[i]:
            stack.append(i)
    while stack:
        cur = stack.pop()
        res.append(cur)
        for v in graph[cur]:
            indegree[v] -= 1
            if not indegree[v]:
                stack.append(v)
    print(*res)


if __name__ == "__main__":
    main()
