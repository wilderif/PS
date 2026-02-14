# BOJ_9335
# 소셜 광고

import sys
import itertools

inp = sys.stdin.readline


def solution():
    n = int(inp())
    graph = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        _, *tmp = map(int, inp().split())
        graph[i].add(i)
        for j in tmp:
            graph[i].add(j)
            graph[j].add(i)

    for i in range(1, n + 1):
        cand = itertools.combinations(range(1, n + 1), i)
        for c in cand:
            tmp = set()
            for j in c:
                tmp |= graph[j]
            if len(tmp) == n:
                return i


def main():
    t = int(inp())
    for _ in range(t):
        print(solution())


if __name__ == "__main__":
    main()
