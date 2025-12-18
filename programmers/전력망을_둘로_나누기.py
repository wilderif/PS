# 전력망을_둘로_나누기


def solution(n, wires):
    def num_nodes():
        vis = [False for _ in range(n + 1)]
        vis[1] = True
        stack = [1]

        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if vis[nxt]:
                    continue
                vis[nxt] = True
                stack.append(nxt)
        return sum(vis)

    graph = [set() for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)

    res = n
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        tmp = num_nodes()
        res = min(res, abs(n - tmp - tmp))
        graph[v1].add(v2)
        graph[v2].add(v1)

    return res
