# BOJ_2056
# 작업

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    time = [0 for _ in range(n + 1)]
    for i in range(n):
        tmp = list(map(int, inp().split()))
        time[i + 1] = tmp[0]
        for j in tmp[2:]:
            graph[j].append(i + 1)
            indeg[i + 1] += 1
    stack = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            stack.append(i)
    res = [0 for _ in range(n + 1)]

    while stack:
        cur = stack.pop()
        res[cur] += time[cur]
        for v in graph[cur]:
            indeg[v] -= 1
            if not indeg[v]:
                stack.append(v)
            res[v] = max(res[cur], res[v])
    print(max(res))


if __name__ == "__main__":
    main()
