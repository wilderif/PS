# 부대복귀


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        vis = [-1 for _ in range(n + 1)]
        vis[start] = 0
        queue = [start]

        while queue:
            new_queue = []

            for cur in queue:
                for nxt in graph[cur]:
                    if vis[nxt] != -1:
                        continue
                    vis[nxt] = vis[cur] + 1
                    new_queue.append(nxt)
            queue = new_queue

        return vis

    dist = bfs(destination)
    res = []
    for s in sources:
        res.append(dist[s])

    return res
