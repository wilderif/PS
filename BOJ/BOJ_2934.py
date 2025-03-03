# BOJ_2934
# LRH 식물

import sys

inp = sys.stdin.readline


def propagate(node, start, end):
    if lazy[node]:
        seg_tree[node] += (end - start + 1) * lazy[node]

        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        lazy[node] = 0


def update(node, start, end, left, right, val):
    propagate(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] += val
        propagate(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, val)
    update(node * 2 + 1, mid + 1, end, left, right, val)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def query(node, start, end, left, right):
    propagate(node, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q_left = query(node * 2, start, mid, left, right)
    q_right = query(node * 2 + 1, mid + 1, end, left, right)

    return q_left + q_right


def main():
    global arr, seg_tree, lazy
    size = 100000
    seg_tree = [0 for _ in range(size * 4)]
    lazy = [0 for _ in range(size * 4)]

    n = int(inp())
    for _ in range(n):
        l, r = map(int, inp().split())
        q_l = query(1, 1, size, l, l)
        q_r = query(1, 1, size, r, r)
        print(q_l + q_r)

        update(1, 1, size, l + 1, r - 1, 1)
        if q_l:
            update(1, 1, size, l, l, -q_l)
        if q_r:
            update(1, 1, size, r, r, -q_r)


if __name__ == "__main__":
    main()
