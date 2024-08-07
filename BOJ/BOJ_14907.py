# BOJ_14907
# 프로젝트 스케줄링

import sys

inp = sys.stdin.readline


def find_index(c):
    return ord(c) - ord("A")


def main():
    graph = [[] for _ in range(26)]
    cost = [0 for _ in range(26)]
    indeg = [0 for _ in range(26)]
    used = set()

    while True:
        try:
            tmp = list(inp().split())
            if not tmp:
                break
            idx = ord(tmp[0]) - ord("A")
            used.add(idx)
            cost[idx] = int(tmp[1])
            if len(tmp) > 2:
                indeg[idx] = len(tmp[2])
                for c in tmp[2]:
                    graph[find_index(c)].append(idx)
        except:
            break
    
    mem = [0 for _ in range(26)]
    stack = []
    for i in used:
        if not indeg[i]:
            stack.append(i)
            mem[i] = cost[i]
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            mem[nxt] = max(mem[nxt], mem[cur] + cost[nxt])
            if not(indeg[nxt]):
                stack.append(nxt)
    res = 0
    for i in used:
        res = max(res, mem[i])
    print(res)


if __name__ == "__main__":
    main()
