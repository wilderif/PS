# BOJ_1202
# 보석 도둑

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    arr1 = [tuple(map(int, inp().split())) for _ in range(n)]
    arr2 = [int(inp()) for _ in range(k)]
    arr1.sort(key=lambda x:x[0], reverse=True)
    arr2.sort()

    max_heap = []
    res = 0
    for i in arr2:
        while arr1 and arr1[-1][0] <= i:
            heapq.heappush(max_heap, -arr1.pop()[1])
        if max_heap:
            res -= heapq.heappop(max_heap)
    print(res)


if __name__ == "__main__":
    main()
