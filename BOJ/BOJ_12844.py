# BOJ_12844
# XOR

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        seg_tree[node] = arr[start]
        return

    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)
    seg_tree[node] = seg_tree[node * 2] ^ seg_tree[node * 2 + 1]


def propagate(node, start, end):
    if lazy[node]:
        if (end - start + 1) % 2:
            seg_tree[node] ^= lazy[node]

        if start != end:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]

        lazy[node] = 0


def update(node, start, end, left, right, val):
    propagate(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] ^= val
        propagate(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, val)
    update(node * 2 + 1, mid + 1, end, left, right, val)
    seg_tree[node] = seg_tree[node * 2] ^ seg_tree[node * 2 + 1]


def query(node, start, end, left, right):
    propagate(node, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q_left = query(node * 2, start, mid, left, right)
    q_right = query(node * 2 + 1, mid + 1, end, left, right)

    return q_left ^ q_right


def main():
    global arr, seg_tree, lazy
    n = int(inp())
    arr = [0] + list(map(int, inp().split()))
    seg_tree = [0 for _ in range(n * 4)]
    lazy = [0 for _ in range(n * 4)]
    init(1, 1, n)

    m = int(inp())
    for _ in range(m):
        inst = list(map(int, inp().split()))
        if inst[0] == 1:
            update(1, 1, n, inst[1] + 1, inst[2] + 1, inst[3])
        else:
            print(query(1, 1, n, inst[1] + 1, inst[2] + 1))


if __name__ == "__main__":
    main()
