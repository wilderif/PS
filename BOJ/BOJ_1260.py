# BOJ_1260
# DFS와 BFS

import sys
from collections import deque

inp = sys.stdin.readline


def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in arr[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, visited)


def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')
    while queue:
        cur = queue.popleft()
        for i in arr[cur]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)


def main():
    global n, m, v, arr
    n, m, v = map(int, inp().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in arr:
        i.sort()
    
    visited = [False] * (n + 1)
    dfs(v, visited)
    print()
    bfs(v)


if __name__ == "__main__":
    main()
