# 네트워크


def solution(n, computers):
    vis = [False for _ in range(n)]
    res = 0

    def dfs(start):
        vis[start] = True
        stack = [start]

        while stack:
            cur = stack.pop()
            for i in range(n):
                nxt = computers[cur][i]
                if not nxt:
                    continue
                if vis[i]:
                    continue
                vis[i] = True
                stack.append(i)

    for i in range(n):
        if vis[i]:
            continue
        res += 1
        dfs(i)

    return res
