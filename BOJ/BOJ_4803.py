# BOJ_4803
# 트리

import sys

inp = sys.stdin.readline


def find(x, parent):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]


def union(u, v, parent, has_cycle):
    u = find(u, parent)
    v = find(v, parent)

    if u == v:
        has_cycle[u] = True
        return False

    if parent[u] > parent[v]:
        u, v = v, u

    if parent[u] == parent[v]:
        parent[u] -= 1

    parent[v] = u

    return True


def main():
    c = 1
    while True:
        n, m = map(int, inp().split())
        if not n and not m:
            return

        print(f"Case {c}: ", end="")
        c += 1

        parent = [-1 for _ in range(n + 1)]
        has_cycle = [False for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, inp().split())
            union(u, v, parent, has_cycle)

        res = 0
        for i in range(1, n + 1):
            if parent[i] < 0 and not has_cycle[i]:
                res += 1
        if res == 0:
            print("No trees.")
        elif res == 1:
            print("There is one tree.")
        else:
            print(f"A forest of {res} trees.")


if __name__ == "__main__":
    main()
