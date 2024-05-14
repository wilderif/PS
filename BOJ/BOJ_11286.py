# BOJ_11286
# 절댓값 힙

import sys

inp = sys.stdin.readline


def swap(heap, idx1, idx2):
    heap[idx1], heap[idx2] = heap[idx2], heap[idx1]


def push(heap, num):
    heap.append(num)
    idx = len(heap) - 1
    while idx > 1:
        if abs(heap[idx]) > abs(heap[idx // 2]):
            break
        elif abs(heap[idx]) == abs(heap[idx // 2]):
            if heap[idx] < heap[idx // 2]:
                swap(heap, idx, idx // 2)
                idx //= 2
            else:
                break
        else:
            swap(heap, idx, idx // 2)
            idx //= 2


def pop(heap):
    if len(heap) == 1:
        print(0)
    else:
        swap(heap, 1, -1)
        print(heap.pop())
        idx = 1
        while idx * 2 < len(heap):
            tmp_idx = idx
            if abs(heap[idx * 2]) < abs(heap[tmp_idx]):
                tmp_idx = idx * 2
            if abs(heap[idx * 2]) == abs(heap[tmp_idx]):
                if heap[idx * 2] < heap[tmp_idx]:
                    tmp_idx = idx * 2
            if idx * 2 + 1 < len(heap) and abs(heap[idx * 2 + 1]) < abs(heap[tmp_idx]):
                tmp_idx = idx * 2 + 1
            if idx * 2 + 1 < len(heap) and abs(heap[idx * 2 + 1]) == abs(heap[tmp_idx]):
                if heap[idx * 2 + 1] < heap[tmp_idx]:
                    tmp_idx = idx * 2 + 1
            
            if idx == tmp_idx:
                break
            else:
                swap(heap, idx, tmp_idx)
                idx = tmp_idx


def main():
    n = int(inp())
    heap = [-1]
    for _ in range(n):
        inst = int(inp())
        if not inst:
            pop(heap)
        else:
            push(heap, inst)


if __name__ == "__main__":
    main()
