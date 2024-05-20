# BOJ_1966
# 프린터 큐

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n, m = map(int, inp().split())
        q = deque(map(int, inp().split()))
        for i in range(len(q)):
            q[i] = [q[i], i]

        cnt = 0
        while True:
            for i in range(len(q)):
                if q[i][0] > q[0][0]:
                    q.append(q.popleft())
                    break
            else:
                tmp = q.popleft()
                cnt += 1
                if tmp[1] == m:
                    break
        print(cnt)

    
if __name__ == "__main__":
    main()
