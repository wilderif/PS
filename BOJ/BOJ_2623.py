# BOJ_2623
# 음악프로그램

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    indeg = [0 for _ in range(n + 1)]
    stack = []
    res = []

    for _ in range(m):
        arr = list(map(int, inp().split()))
        if arr[0] > 1:
            for i in range(1, arr[0]):
                graph[arr[i]].append(arr[i + 1])
                indeg[arr[i + 1]] += 1
    
    for i in range(1, n + 1):
        if not indeg[i]:
            stack.append(i)
            res.append(i)

    while stack:
        cur = stack.pop()
        
        for v in graph[cur]:
            indeg[v] -= 1
            if not indeg[v]:
                stack.append(v)
                res.append(v)

    if len(res) == n:
        for i in res:
            print(i)
    else:
        print(0)


if __name__ == "__main__":
    main()
