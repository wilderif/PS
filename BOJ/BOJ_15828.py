# BOJ_15828
# Router

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n = int(inp())
    dq = deque()
    while True:
        a = int(inp())
        if a == -1:
            break
        if a == 0:
            dq.popleft()
        else:
            if len(dq) < n:
                dq.append(a)
    if dq:
        print(*dq)
    else:
        print("empty")


if __name__ == "__main__":
    main()
