# BOJ_2606
# 바이러스

import sys
from collections import deque


def solution():
    n = int(input())
    t = int(input())
    rel = [[] for _ in range(n + 1)]

    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        rel[a].append(b)
        rel[b].append(a)

    queue = deque([1])
    visit = [1]

    while queue:
        c = queue.popleft()
        for i in rel[c]:
            if i not in visit:
                visit.append(i)
                queue.append(i)
    print(len(visit) - 1)


if __name__ == "__main__":
    solution()
