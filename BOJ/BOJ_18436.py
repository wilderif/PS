# BOJ_18436
# 수열과 쿼리 37

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        if arr[start] % 2:
            seg_tree[node] = 1
        else:
            seg_tree[node] = 0
        return

    mid = (start + end) // 2
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    seg_tree[node] = seg_tree[2 * node] + seg_tree[2 * node + 1]


def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q1 = query(2 * node, start, mid, left, right)
    q2 = query(2 * node + 1, mid + 1, end, left, right)
    return q1 + q2


def update(node, start, end, idx, val):
    if idx < start or end < idx:
        return

    if start == end:
        if val % 2:
            seg_tree[node] = 1
        else:
            seg_tree[node] = 0
        return

    mid = (start + end) // 2
    update(2 * node, start, mid, idx, val)
    update(2 * node + 1, mid + 1, end, idx, val)

    seg_tree[node] = seg_tree[2 * node] + seg_tree[2 * node + 1]


def main():
    global seg_tree, arr
    n = int(inp())

    arr = [0] + list(map(int, inp().split()))
    seg_tree = [0 for _ in range(4 * n)]
    init(1, 1, n)

    m = int(inp())
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if a == 1:
            update(1, 1, n, b, c)
        elif a == 2:
            ret = query(1, 1, n, b, c)
            print(c + 1 - b - ret)
        else:
            ret = query(1, 1, n, b, c)
            print(ret)


if __name__ == "__main__":
    main()
