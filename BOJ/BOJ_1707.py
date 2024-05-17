# BOJ_1707
# 이분 그래프

import sys

inp = sys.stdin.readline


def main():
    k = int(inp())
    for _ in range(k):
        v, e = map(int, inp().split())
        graph = [[] for _ in range(v + 1)]
        for _ in range(e):
            a, b = map(int, inp().split())
            graph[a].append(b)
            graph[b].append(a)
        visited = [-1 for _ in range(v + 1)]

        flag = True
        for i in range(1, v + 1):
            stack = []
            if visited[i] == -1:
                stack.append(i)
                visited[i] = 0
                while stack:
                    cur = stack.pop()
                    cur_color = visited[cur]
                    for next in graph[cur]:
                        if visited[next] == -1:
                            stack.append(next)
                            visited[next] = (cur_color + 1) % 2
                        else:
                            if visited[next] == cur_color:
                                flag = False
                                break
                    if not flag:
                        break
            if not flag:
                break
        if flag:
            print("YES")
        else:
            print("NO")
        
    
if __name__ == "__main__":
    main()
