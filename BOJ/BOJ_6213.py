# BOJ_6213
# Balanced Lineup

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        seg_tree[node] = [arr[start], arr[start]]
        return

    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

    seg_tree[node][0] = min(seg_tree[node * 2][0], seg_tree[node * 2 + 1][0])
    seg_tree[node][1] = max(seg_tree[node * 2][1], seg_tree[node * 2 + 1][1])


def query(node, start, end, left, right):
    if right < start or end < left:
        return [10**6, 0]

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q_left = query(node * 2, start, mid, left, right)
    q_right = query(node * 2 + 1, mid + 1, end, left, right)

    return (min(q_left[0], q_right[0]), max(q_left[1], q_right[1]))


def main():
    global seg_tree, arr
    n, q = map(int, inp().split())
    arr = [0] + [int(inp()) for _ in range(n)]
    seg_tree = [[10**6, 0] for _ in range(n * 4)]

    init(1, 1, n)

    for _ in range(q):
        a, b = map(int, inp().split())
        ret = query(1, 1, n, a, b)
        print(ret[1] - ret[0])


if __name__ == "__main__":
    main()
