# BOJ_1412
# 일방통행

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = inp().rstrip()
        for j in range(n):
            if tmp[j] == 'Y':
                graph[i][j] = True
    
    graph_2 = [[] for _ in range(n)]
    indeg = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] and not graph[j][i]:
                graph_2[i].append(j)
                indeg[j] += 1
    
    stack = []
    for i in range(n):
        if not indeg[i]:
            stack.append(i)
    while stack:
        cur = stack.pop()
        for nxt in graph_2[cur]:
            indeg[nxt] -= 1
            if not indeg[nxt]:
                stack.append(nxt)
    
    for i in indeg:
        if i:
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
