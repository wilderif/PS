# BOJ_2611
# 자동차경주

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    for _ in range(m):
        p, q, r = map(int, inp().split())
        graph[p].append((q, r))
        indeg[q] += 1
    
    mem = [0 for _ in range(n + 1)]
    prev = [0 for _ in range(n + 1)]
    indeg[1] = 0
    stack = []
    stack.append(1)

    while stack:
        cur = stack.pop()
        for nxt, cost in graph[cur]:
            if mem[nxt] < mem[cur] + cost:
                mem[nxt] = mem[cur] + cost
                prev[nxt] = cur
            indeg[nxt] -= 1
            if not indeg[nxt]:
                stack.append(nxt)

    res_path = [1]
    res_path.append(prev[1])
    while res_path[-1] != 1:
        res_path.append(prev[res_path[-1]])
        
    print(mem[1])
    for i in range(len(res_path) - 1, -1, -1):
        print(res_path[i], end=' ')
    

if __name__ == "__main__":
    main()
