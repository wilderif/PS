# BOJ_10868
# 최솟값

import sys

inp = sys.stdin.readline


def build():
    for i in range(size - 1, 0, -1):
        seg_tree[i] = min(seg_tree[i * 2], seg_tree[i * 2 + 1])


def find(left, right):
    ret = 10**10
    left += size - 1
    right += size - 1

    while left <= right:
        if left % 2:
            ret = min(ret, seg_tree[left])
        if not right % 2:
            ret = min(ret, seg_tree[right])
        left = (left + 1) // 2
        right = (right - 1) // 2
    return ret


def main():
    global size, seg_tree
    n, m = map(int, inp().split())
    arr = [int(inp()) for _ in range(n)]

    size = 1
    while size < n:
        size *= 2
    seg_tree = [0 for _ in range(size * 2)]
    for i in range(n):
        seg_tree[size + i] = arr[i]

    build()
    for _ in range(m):
        a, b = map(int, inp().split())
        print(find(a, b))


if __name__ == "__main__":
    main()
