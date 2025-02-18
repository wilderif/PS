# BOJ_17619
# 개구리 점프

import sys

inp = sys.stdin.readline


def main():
    n, q = map(int, inp().split())
    arr = []
    for i in range(n):
        arr.append((i + 1, tuple(map(int, inp().split()))))
    arr.sort(key=lambda x: x[1][0])

    parent = [-1 for _ in range(n + 1)]

    def find(x):
        if parent[x] < 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False

        if parent[root_u] > parent[root_v]:
            root_u, root_v = root_v, root_u

        if parent[root_u] == parent[root_v]:
            parent[root_u] -= 1

        parent[root_v] = root_u
        return True

    cur_max = arr[0][1][1]

    for i in range(1, n):
        if arr[i][1][0] <= cur_max:
            union(arr[i - 1][0], arr[i][0])
        cur_max = max(cur_max, arr[i][1][1])

    res = []
    for _ in range(q):
        a, b = map(int, inp().split())
        if find(a) == find(b):
            # print(1)
            res.append(1)
        else:
            # print(0)
            res.append(0)

    sys.stdout.write("\n".join(map(str, res)))


if __name__ == "__main__":
    main()
