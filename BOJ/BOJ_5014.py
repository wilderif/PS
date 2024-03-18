# BOJ_5014
# 스타트링크

import sys
from collections import deque


def main():
    f, s, g, u, d = map(int, sys.stdin.readline().split())
    vis = [-1 for _ in range(f + 1)]
    q = deque()
    q.append(s)
    vis[s] = 0

    while q:
        cur = q.popleft()
        for i in [cur + u, cur - d]:
            if 0 < i <= f and vis[i] == -1:
                q.append(i)
                vis[i] = vis[cur] + 1
        if vis[g] != -1:
            print(vis[g])
            return None
    else:
        print("use the stairs")


if __name__ == "__main__":
    main()
