# BOJ_20303
# 할로윈의 양아치

import sys

inp = sys.stdin.readline


def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(u, v):
    u_root = find(u)
    v_root = find(v)

    if u_root == v_root:
        return False

    if u_root > v_root:
        u_root, v_root = v_root, u_root

    if parent[u_root] == parent[v_root]:
        parent[u_root] -= 1

    parent[v_root] = u_root

    return True


def main():
    global parent
    n, m, k = map(int, inp().split())
    arr = [-1] + list(map(int, inp().split()))
    parent = [-1 for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, inp().split())
        union(a, b)

    group_map = {}
    for i in range(1, n + 1):
        group_idx = find(i)
        group_map[group_idx] = group_map.get(group_idx, [0, 0])
        group_map[group_idx][0] += 1
        group_map[group_idx][1] += arr[i]

    group_list = list(group_map.values())

    dp = [0 for _ in range(k)]
    for weight, value in group_list:
        for w in range(k - 1, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    print(dp[-1])


if __name__ == "__main__":
    main()
