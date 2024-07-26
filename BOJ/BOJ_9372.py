# BOJ_9372
# 상근이의 여행

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n, m = map(int, inp().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, inp().split())
            graph[a].append(b)
            graph[b].append(a)
        
        used = [False for _ in range(n + 1)]
        nxt = []
        for e in graph[1]:
            nxt.append(e)
        used[1] = True

        res = 0
        while nxt:
            cur = nxt.pop()
            if used[cur]:
                continue
            used[cur] = True
            res += 1
            
            for e in graph[cur]:
                if not used[e]:
                    nxt.append(e)
        print(res)
    
        
if __name__ == "__main__":
    main()
