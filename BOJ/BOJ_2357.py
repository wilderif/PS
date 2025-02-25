# BOJ_2357
# 최솟값과 최댓값

import sys

inp = sys.stdin.readline


def build(idx, left, right):
    if left == right:
        seg_tree[idx][0] = arr[left]
        seg_tree[idx][1] = arr[left]
        return seg_tree[idx]

    mid = (left + right) // 2
    left_val = build(idx * 2, left, mid)
    right_val = build(idx * 2 + 1, mid + 1, right)
    seg_tree[idx][0] = min(left_val[0], right_val[0])
    seg_tree[idx][1] = max(left_val[1], right_val[1])
    return seg_tree[idx]


def find(idx, left, right, start, end):
    if left > end or right < start:
        return [10**9, 0]

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left + right) // 2
    left_val = find(idx * 2, left, mid, start, end)
    right_val = find(idx * 2 + 1, mid + 1, right, start, end)
    return [min(left_val[0], right_val[0]), max(left_val[1], right_val[1])]


def main():
    global arr, seg_tree
    n, m = map(int, inp().split())
    arr = [0] + [int(inp()) for _ in range(n)]
    seg_tree = [[10**9, 0] for _ in range(n * 4)]

    build(1, 1, n)

    for _ in range(m):
        a, b = map(int, inp().split())
        print(*find(1, 1, n, a, b))


if __name__ == "__main__":
    main()
