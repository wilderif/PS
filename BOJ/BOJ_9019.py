# BOJ_9019
# DSLR

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        a, b = map(int, inp().split())
        vis = [None for _ in range(10000)]
        q = deque()
        q.append(a)
        vis[a] = ""

        while vis[b] is None:
            cur = q.popleft()

            nxt = (cur * 2) % 10000
            if vis[nxt] is None:
                vis[nxt] = vis[cur] + "D"
                q.append(nxt)

            if cur == 0:
                nxt = 9999
            else:
                nxt = cur - 1
            if vis[nxt] is None:
                vis[nxt] = vis[cur] + "S"
                q.append(nxt)

            nxt = (cur % 1000) * 10 + (cur // 1000)
            if vis[nxt] is None:
                vis[nxt] = vis[cur] + "L"
                q.append(nxt)

            nxt = (cur % 10) * 1000 + (cur // 10)
            if vis[nxt] is None:
                vis[nxt] = vis[cur] + "R"
                q.append(nxt)
        print(vis[b])
        

if __name__ == "__main__":
    main()
