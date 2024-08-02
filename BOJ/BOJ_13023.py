# BOJ_13023
# ABCDE

import sys

inp = sys.stdin.readline


def dfs(graph, cur, vis, depth):
    if depth == 4:
        print(1)
        sys.exit()
    for nxt in graph[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            dfs(graph, nxt, vis, depth + 1)
            vis[nxt] = False


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
        graph[b].append(a)
    
    vis = [False for _ in range(n)]
    for i in range(n):
        vis[i] = True
        dfs(graph, i, vis, 0)
        vis[i] = False
        
    print(0)


if __name__ == "__main__":
    main()
