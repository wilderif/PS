# BOJ_1275
# 커피숍2

import sys

inp = sys.stdin.readline


def build():
    for i in range(size - 1, 0, -1):
        seg_tree[i] = seg_tree[i * 2] + seg_tree[i * 2 + 1]


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
    global seg_tree, size
    n, q = map(int, inp().split())
    arr = list(map(int, inp().split()))
    size = 1
    while size < n:
        size *= 2
    seg_tree = [0 for _ in range(size * 2)]
    for i in range(n):
        seg_tree[size + i] = arr[i]

    build()

    for _ in range(q):
        x, y, a, b = map(int, inp().split())
        x, y = (y, x) if x > y else (x, y)
        print(find(x, y))
        update(a, b)


if __name__ == "__main__":
    main()
