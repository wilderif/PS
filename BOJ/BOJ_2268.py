# BOJ_2268
# 수들의 합 7

import sys

inp = sys.stdin.readline


def find(left, right):
    ret = 0
    left += size - 1
    right += size - 1

    while left <= right:
        if left % 2:
            ret += seg_tree[left]
        if not right % 2:
            ret += seg_tree[right]
        left = (left + 1) // 2
        right = (right - 1) // 2
    return ret


def update(idx, val):
    idx += size - 1
    seg_tree[idx] = val
    while idx > 1:
        idx //= 2
        seg_tree[idx] = seg_tree[idx * 2] + seg_tree[idx * 2 + 1]


def main():
    global size, seg_tree
    n, m = map(int, inp().split())

    size = 1
    while size < n:
        size *= 2
    seg_tree = [0 for _ in range(size * 2)]

    for _ in range(m):
        a, b, c = map(int, inp().split())
        if a:
            update(b, c)
        else:
            (b, c) = (c, b) if b > c else (b, c)
            print(find(b, c))


if __name__ == "__main__":
    main()
