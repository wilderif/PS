# BOJ_2668
# 숫자고르기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [None] + [int(inp()) for _ in range(n)]
    vis = [False for _ in range(n + 1)]
    res = []
    for i in range(1, n + 1):
        path = []
        used = set()
        cur = i
        while cur not in used and not vis[cur]:
            vis[cur] = True
            used.add(cur)
            path.append(cur)
            cur = arr[cur]

        flag = False
        for j in path:
            # cycle이 만들어질 때부터 방문한 노드들 res에 추가
            if not flag and j == cur:
                flag = True
            if flag:
                res.append(j)

    print(len(res))
    print("\n".join(map(str, sorted(res))))


if __name__ == "__main__":
    main()
