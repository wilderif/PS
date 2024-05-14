# BOJ_13549
# 숨바꼭질 3

import sys
from collections import deque


def main():
    n, k = map(int, sys.stdin.readline().split())
    max_range = None
    if k <= n:
        print(n - k)
        return
    else:
        max_range = k * 2 + 1
    vis = [-1 for _ in range(max_range)]
    q = deque()
    tmp_q = deque()
    vis[n] = 0
    q.append(n)
    while vis[k] == -1:
        while q:
            cur = q.popleft()
            tmp_q.append(cur)
            tmp = cur * 2
            while 0 < tmp < max_range:
                if vis[tmp] == -1:
                    vis[tmp] = vis[cur]
                tmp_q.append(tmp)
                tmp *= 2
        while tmp_q:
            cur = tmp_q.popleft()
            if 0 <= cur - 1 < max_range and vis[cur - 1] == -1:
                vis[cur - 1] = vis[cur] + 1
                q.append(cur - 1)
            if 0 <= cur + 1 < max_range and vis[cur + 1] == -1:
                vis[cur + 1] = vis[cur] + 1
                q.append(cur + 1)

    print(vis[k])
    

if __name__ == "__main__":
    main()
