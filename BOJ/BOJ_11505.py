# BOJ_11505
# 구간 곱 구하기

import sys

inp = sys.stdin.readline


mod = 1000000007


def build():
    for i in range(size - 1, 0, -1):
        seg_tree[i] = seg_tree[i * 2] * seg_tree[i * 2 + 1] % mod


def find(left, right):
    ret = 1
    left += size - 1
    right += size - 1

    while left <= right:
        if left % 2:
            ret = ret * seg_tree[left] % mod
        if not right % 2:
            ret = ret * seg_tree[right] % mod
        left = (left + 1) // 2
        right = (right - 1) // 2
    return ret


def update(idx, val):
    idx += size - 1
    seg_tree[idx] = val
    while idx > 1:
        idx //= 2
        seg_tree[idx] = seg_tree[idx * 2] * seg_tree[idx * 2 + 1] % mod


def main():
    global seg_tree, size
    n, m, k = map(int, inp().split())
    size = 1
    while size < n:
        size *= 2

    seg_tree = [1 for _ in range(size * 2)]
    for i in range(n):
        seg_tree[size + i] = int(inp())

    build()

    for _ in range(m + k):
        a, b, c = map(int, inp().split())
        if a == 1:
            update(b, c)
        else:
            print(find(b, c))


if __name__ == "__main__":
    main()
