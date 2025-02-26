# BOJ_14438
# 수열과 쿼리 17

import sys

inp = sys.stdin.readline


def build():
    for i in range(size - 1, 0, -1):
        seg_tree[i] = min(seg_tree[i * 2], seg_tree[i * 2 + 1])


def find(left, right):
    ret = 10**10 + 1
    left += size - 1
    right += size - 1

    while left <= right:
        if left & 1:
            ret = min(ret, seg_tree[left])
        if right & 1 == 0:
            ret = min(ret, seg_tree[right])
        left = (left + 1) >> 1
        right = (right - 1) >> 1

    return ret


def update(idx, val):
    idx += size - 1
    seg_tree[idx] = val
    while idx > 1:
        idx >>= 1
        seg_tree[idx] = min(seg_tree[idx * 2], seg_tree[idx * 2 + 1])


def main():
    global size, seg_tree
    n = int(inp())
    arr = list(map(int, inp().split()))

    size = 1
    while size < n:
        size *= 2
    seg_tree = [10**10 + 1 for _ in range(size * 2)]
    for i in range(n):
        seg_tree[size + i] = arr[i]

    build()

    m = int(inp())
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if a == 1:
            update(b, c)
        else:
            print(find(b, c))


if __name__ == "__main__":
    main()
