# BOJ_1168
# 요세푸스 문제 2

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        seg_tree[node] = 1
        return

    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def query(node, start, end, target_idx):
    seg_tree[node] -= 1
    if start == end:
        return start

    mid = (start + end) // 2
    left_val = seg_tree[node * 2]

    if left_val > target_idx:
        return query(node * 2, start, mid, target_idx)
    else:
        return query(node * 2 + 1, mid + 1, end, target_idx - left_val)


def update(node, start, end, idx):
    if idx < start or end < idx:
        return

    if start == end:
        seg_tree[node] = 0
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, idx)
    update(node * 2 + 1, mid + 1, end, idx)

    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def main():
    global seg_tree
    n, k = map(int, inp().split())
    seg_tree = [0 for _ in range(n * 4)]
    init(1, 1, n)

    res = []
    idx = 0

    for _ in range(n):
        idx = (idx + k - 1) % (n - len(res))
        ret = query(1, 1, n, idx)
        res.append(ret)
        # update(1, 1, n, ret)

    print("<", end="")
    print(", ".join(map(str, res)), end=">")


if __name__ == "__main__":
    main()
