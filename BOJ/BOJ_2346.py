# BOJ_2346
# 풍선 터뜨리기

import sys
from collections import deque
inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    dq = deque()
    for i in range(n):
        dq.append([arr[i], i + 1])
    res = []
    while dq:
        cur = dq.popleft()
        res.append(cur[1])
        if dq:
            if cur[0] > 0:
                for _ in range(cur[0] - 1):
                    dq.append(dq.popleft())
            else:
                for _ in range(-cur[0]):
                    dq.appendleft(dq.pop())
    print(*res)


if __name__ == "__main__":
    main()
