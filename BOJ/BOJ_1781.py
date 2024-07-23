# BOJ_1781
# 컵라면

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [tuple(map(int, inp().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])
    max_heap = []
    res = 0
    for i in range(n, 0, -1):
        while arr and arr[-1][0] >= i:
            heapq.heappush(max_heap, -arr.pop()[1])
        if max_heap:
            res -= heapq.heappop(max_heap)
    print(res)


if __name__ == "__main__":
    main()
