# BOJ_13334
# 철로

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = []
    for _ in range(n):
        a, b = map(int, inp().split())
        if a > b:
            a, b = b, a
        arr.append((a, b))
    arr.sort(key=lambda x: (x[1], x[0]))
    d = int(inp())

    res = 0
    min_heap = []
    cur_start = -(10**8)

    for el in arr:
        heapq.heappush(min_heap, el[0])
        while min_heap:
            cur_start = min_heap[0]
            if el[1] <= cur_start + d:
                break
            else:
                heapq.heappop(min_heap)
        res = max(res, len(min_heap))

    print(res)
    return


if __name__ == "__main__":
    main()
