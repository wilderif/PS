# BOJ_12851
# 숨바꼭질 2

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    vis = [[-1, 0] for _ in range(max(n, k) + 2)]

    q = deque()
    q.append(n)
    vis[n][0] = 0
    vis[n][1] = 1
    
    while q:
        cur = q.popleft()
        if vis[k][0] != -1 and vis[cur][0] > vis[k][0]:
            break
        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt < len(vis):
                if vis[nxt][0] == -1 or vis[nxt][0] == vis[cur][0] + 1:
                    if vis[nxt][0] == -1:
                        q.append(nxt)
                    vis[nxt][0] = vis[cur][0] + 1
                    vis[nxt][1] += vis[cur][1]

    print(vis[k][0])
    print(vis[k][1])


if __name__ == "__main__":
    main()
