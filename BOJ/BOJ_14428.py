# BOJ_14428
# 수열과 쿼리 16

import sys

inp = sys.stdin.readline


def comp(idx):
    if seg_tree[idx * 2][0] <= seg_tree[idx * 2 + 1][0]:
        return seg_tree[idx * 2][:]

    else:
        return seg_tree[idx * 2 + 1][:]


def build():
    for i in range(size - 1, 0, -1):
        seg_tree[i] = comp(i)


def find(left, right):
    ret = [10**10 + 1, -1]
    left += size - 1
    right += size - 1

    while left <= right:
        if left & 1:
            if ret[0] > seg_tree[left][0] or (
                ret[0] == seg_tree[left][0] and ret[1] > seg_tree[left][1]
            ):
                ret = seg_tree[left][:]
            left += 1
        if right & 1 == 0:
            if ret[0] > seg_tree[right][0] or (
                ret[0] == seg_tree[right][0] and ret[1] > seg_tree[right][1]
            ):
                ret = seg_tree[right][:]
            right -= 1
        left >>= 1
        right >>= 1

    return ret[1]


def update(idx, val):
    idx += size - 1
    seg_tree[idx][0] = val
    while idx > 1:
        idx >>= 1
        seg_tree[idx] = comp(idx)


def main():
    global size, seg_tree
    n = int(inp())
    arr = list(map(int, inp().split()))

    size = 1
    while size < n:
        size *= 2
    seg_tree = [[10**10 + 1, 0] for _ in range(size * 2)]
    for i in range(n):
        seg_tree[size + i] = [arr[i], i + 1]

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
