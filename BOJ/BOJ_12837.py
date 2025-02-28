# BOJ_12837
# 가계부 (Hard)

import sys

inp = sys.stdin.readline


def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q_left = query(node * 2, start, mid, left, right)
    q_right = query(node * 2 + 1, mid + 1, end, left, right)

    return q_left + q_right


def update(node, start, end, idx, val):
    if idx < start or end < idx:
        return

    if start == end:
        seg_tree[node] += val
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)

    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def main():
    global seg_tree
    n, q = map(int, inp().split())
    seg_tree = [0 for _ in range(n * 4)]
    for _ in range(q):
        a, b, c = map(int, inp().split())
        if a == 1:
            update(1, 1, n, b, c)
        elif a == 2:
            print(query(1, 1, n, b, c))


if __name__ == "__main__":
    main()
