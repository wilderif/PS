# SWEA_2814
# 최장 경로


def solution():
    n, m = map(int, input().split())
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)

    ret = 0

    def dfs(cur_node, vis, depth):
        nonlocal ret
        ret = max(ret, depth)
        for nxt_node in graph[cur_node]:
            if nxt_node in vis:
                continue
            vis.add(nxt_node)
            dfs(nxt_node, vis, depth + 1)
            vis.remove(nxt_node)

    for start in range(1, n + 1):
        vis = set()
        vis.add(start)
        dfs(start, vis, 1)
        if ret == n:
            return ret

    return ret


def main():
    t = int(input())
    for tc in range(t):
        res = solution()
        print(f"#{tc + 1} {res}")


main()
