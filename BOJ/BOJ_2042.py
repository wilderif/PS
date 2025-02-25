# BOJ_2042
# 구간 합 구하기

import sys

inp = sys.stdin.readline


# idx - seg_tree의 index
# left, right - 원본 배열의 탐색 범위
def build(idx, left, right):
    if left == right:
        seg_tree[idx] = arr[left]
        return seg_tree[idx]

    mid = (left + right) // 2
    left_val = build(idx * 2, left, mid)
    right_val = build(idx * 2 + 1, mid + 1, right)
    seg_tree[idx] = left_val + right_val
    return seg_tree[idx]


def find(idx, left, right, start, end):
    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return seg_tree[idx]

    mid = (left + right) // 2
    left_val = find(idx * 2, left, mid, start, end)
    right_val = find(idx * 2 + 1, mid + 1, right, start, end)
    return left_val + right_val


def update(idx, left, right, target_idx, val):
    if target_idx < left or right < target_idx:
        return

    if left == right == target_idx:
        seg_tree[idx] = val
        return

    mid = (left + right) // 2
    update(idx * 2, left, mid, target_idx, val)
    update(idx * 2 + 1, mid + 1, right, target_idx, val)

    seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]


def main():
    global arr, seg_tree
    n, m, k = map(int, inp().split())
    arr = [None] + [int(inp()) for _ in range(n)]
    seg_tree = [0 for _ in range(4 * n)]
    build(1, 1, n)

    for _ in range(m + k):
        a, b, c = map(int, inp().split())
        if a == 1:
            update(1, 1, n, b, c)
        else:
            print(find(1, 1, n, b, c))


if __name__ == "__main__":
    main()
