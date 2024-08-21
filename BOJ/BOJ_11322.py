# BOJ_11322
# Numbers are Easy

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        q = deque()
        q.append(1)
        while True:
            cur = q.popleft()
            if not cur % n:
                print(cur)
                break
            q.append(cur * 10)
            q.append(cur * 10 + 1)


if __name__ == "__main__":
    main()
