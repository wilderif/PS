# BOJ_16928
# 뱀과 사다리 게임

import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    ladder_snake = [0 for _ in range(101)]
    for _ in range(n + m):
        s, e = map(int, sys.stdin.readline().split())
        ladder_snake[s] = e
    
    vis = [100 for _ in range(101)]
    queue = deque()
    vis[1] = 0
    queue.append(1)
    while vis[100] == 100:
        cur = queue.popleft()
        cur_time = vis[cur]
        for i in range(1, 7):
            next = cur + i
            if next < 101:
                if ladder_snake[next]:
                    if vis[ladder_snake[next]] > cur_time + 1:
                        vis[ladder_snake[next]] = cur_time + 1
                        queue.append(ladder_snake[next])
                else:
                    if vis[next] > cur_time + 1:
                        vis[next] = cur_time + 1
                        queue.append(next)
        
    print(vis[100])
    

if __name__ == "__main__":
    main()
