# BOJ_25418
# 정수 a를 k로 만들기

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    a, k = map(int, inp().split())
    vis = [-1 for _ in range(k + 1)]
    q = deque()
    q.append(a)
    vis[a] = 0

    while vis[k] == -1:
        cur = q.popleft()
        if cur * 2 <= k:
            if vis[cur * 2] == -1:
                q.append(cur * 2)
                vis[cur * 2] = vis[cur] + 1
        if vis[cur + 1] == -1:
            q.append(cur + 1)
            vis[cur + 1] = vis[cur] + 1
    
    print(vis[k])
            

if __name__ == "__main__":
    main()