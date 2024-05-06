# BOJ_5567
# 결혼식

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque()
    visited = [-1 for _ in range(n + 1)] 
    queue.append(1)
    visited[1] = 0
    res = 0
    while queue:
        cur = queue.popleft()
        cur_time = visited[cur]
        if cur_time == 2:
            break
        for i in graph[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur] + 1
                res += 1
                queue.append(i)
    print(res)


if __name__ == "__main__":
    main()
