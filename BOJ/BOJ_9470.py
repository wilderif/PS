# BOJ_9470
# Strahler 순서

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        k, m, p = map(int, inp().split())
        graph = [[] for _ in range(m + 1)]
        indeg = [0 for _ in range(m + 1)]
        level = [0 for _ in range(m + 1)]
        check = [0 for _ in range(m + 1)]

        for _ in range(p):
            a, b = map(int, inp().split())
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque()
        for i in range(1, m + 1):
            if not indeg[i]:
                level[i] = 1
                q.append(i)
        
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if level[nxt] == level[cur]:
                    if not check[nxt]:
                        check[nxt] += 1
                    elif check[nxt] == 1:
                        level[nxt] += 1
                        check[nxt] = 2
                elif level[nxt] < level[cur]:
                    level[nxt] = level[cur]
                    check[nxt] = 1
                if not indeg[nxt]:
                    q.append(nxt)
        
        print(k, level[m])


if __name__ == "__main__":
    main()
