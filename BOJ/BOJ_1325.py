# BOJ_1325
# 효율적인 해킹

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[b].append(a)

    res = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        tmp = 0
        stack = []
        vis = [False for _ in range(n + 1)]
        stack.append(i)
        tmp += 1
        vis[i] = True
        while stack:
            cur = stack.pop()
            for next in graph[cur]:
                if not vis[next]:
                    vis[next] = True
                    stack.append(next)
                    tmp += 1
        res[i] = tmp
    check = max(res)
    for i in range(1, n + 1):
        if res[i] == check:
            print(i[0], end=' ')


if __name__ == "__main__":
    main()
