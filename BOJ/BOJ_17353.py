# BOJ_17353
# 하늘에서 떨어지는 1, 2, ..., R-L+1개의 별

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
    n = int(inp())
    arr = [0] + list(map(int, inp().split()))
    seg_tree = [0 for _ in range(n * 4)]
    lazy = [0 for _ in range(n * 4)]

    q = int(inp())
    for _ in range(q):
        inst = list(map(int, inp().split()))
        if inst[0] == 1:
            l, r = inst[1], inst[2]
            update(1, 1, n, l, r, 1)
            update(1, 1, n, r + 1, r + 1, -(r - l + 1))
        else:
            print(query(1, 1, n, 1, inst[1]) + arr[inst[1]])


if __name__ == "__main__":
    main()
