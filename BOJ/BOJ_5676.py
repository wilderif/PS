# BOJ_5676
# 음주 코딩

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        if arr[start] > 0:
            seg_tree[node] = 1
        elif arr[start] == 0:
            seg_tree[node] = 0
        else:
            seg_tree[node] = -1
        return

    mid = (start + end) // 2
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    seg_tree[node] = seg_tree[2 * node] * seg_tree[2 * node + 1]


def query(node, start, end, left, right):
    if right < start or end < left:
        return 1

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q1 = query(2 * node, start, mid, left, right)
    q2 = query(2 * node + 1, mid + 1, end, left, right)
    return q1 * q2


def update(node, start, end, idx, val):
    if idx < start or end < idx:
        return

    if start == end:
        if val > 0:
            seg_tree[node] = 1
        elif val == 0:
            seg_tree[node] = 0
        else:
            seg_tree[node] = -1
        return

    mid = (start + end) // 2
    update(2 * node, start, mid, idx, val)
    update(2 * node + 1, mid + 1, end, idx, val)

    seg_tree[node] = seg_tree[2 * node] * seg_tree[2 * node + 1]


def main():
    global seg_tree, arr
    while True:
        try:
            n, k = map(int, inp().split())
            arr = [0] + list(map(int, inp().split()))
            seg_tree = [0 for _ in range(4 * n)]
            init(1, 1, n)

            res = ""
            for _ in range(k):
                inst, a, b = inp().split()
                if inst == "C":
                    update(1, 1, n, int(a), int(b))
                elif inst == "P":
                    ret = query(1, 1, n, int(a), int(b))
                    if ret > 0:
                        res += "+"
                    elif ret == 0:
                        res += "0"
                    else:
                        res += "-"

            print(res)
        except:
            break


if __name__ == "__main__":
    main()
