# BOJ_1395
# 스위치

import sys

inp = sys.stdin.readline


def propagate(node, start, end):
    if lazy[node]:
        seg_tree[node] = (end - start + 1) - seg_tree[node]

        if start != end:
            lazy[node * 2] = not lazy[node * 2]
            lazy[node * 2 + 1] = not lazy[node * 2 + 1]

        lazy[node] = False


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


def update(node, start, end, left, right):
    propagate(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] = not lazy[node]
        propagate(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right)
    update(node * 2 + 1, mid + 1, end, left, right)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def main():
    global seg_tree, lazy
    n, m = map(int, inp().split())
    seg_tree = [0 for _ in range(n * 4)]
    lazy = [False for _ in range(n * 4)]

    for _ in range(m):
        o, s, t = map(int, inp().split())
        if not o:
            update(1, 1, n, s, t)
        else:
            print(query(1, 1, n, s, t))


if __name__ == "__main__":
    main()
