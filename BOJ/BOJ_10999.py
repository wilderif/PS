# BOJ_10999
# 구간 합 구하기 2

import sys

inp = sys.stdin.readline


def init(node, start, end):
    if start == end:
        seg_tree[node] = arr[start]
        return

    mid = (start + end) // 2
    init(node * 2, start, mid)
    init(node * 2 + 1, mid + 1, end)

    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def propagate(node, start, end):
    # 없데이트 되지 않은 값이 있을 때,
    if lazy[node]:
        # seg_tree의 해당 노드는 구간만큼 더해 줌
        seg_tree[node] += (end - start + 1) * lazy[node]

        # 자식 노드로 lazy 값 전파
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        # 업데이트 완료했으므로 lazy 배열의 해당 node 초기화
        lazy[node] = 0


def query(node, start, end, left, right):
    # 해당 노드에 lazy 값이 있으면 더해준 뒤 계산
    propagate(node, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[node]

    mid = (start + end) // 2
    q_left = query(node * 2, start, mid, left, right)
    q_right = query(node * 2 + 1, mid + 1, end, left, right)

    return q_left + q_right


def update(node, start, end, left, right, val):
    propagate(node, start, end)
    if right < start or end < left:
        return

    if left <= start and end <= right:
        # 범위에 들어올 때는 propagate() 내부에서 자식 개수만큼 seg_tree 값 변경
        lazy[node] += val
        propagate(node, start, end)
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, val)
    update(node * 2 + 1, mid + 1, end, left, right, val)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]


def main():
    global arr, seg_tree, lazy
    n, m, k = map(int, inp().split())
    arr = [0] + [int(inp()) for _ in range(n)]
    seg_tree = [0 for _ in range(n * 4)]
    lazy = [0 for _ in range(n * 4)]

    init(1, 1, n)

    for _ in range(m + k):
        inst, *tmp = tuple(map(int, inp().split()))
        if inst == 1:
            update(1, 1, n, tmp[0], tmp[1], tmp[2])
        else:
            print(query(1, 1, n, tmp[0], tmp[1]))


if __name__ == "__main__":
    main()
