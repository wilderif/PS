# BOJ_1715
# 카드 정렬하기

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    heap = [int(inp()) for _ in range(n)]
    heapq.heapify(heap)
    res = 0
    while len(heap) > 1:
        tmp = heapq.heappop(heap) + heapq.heappop(heap)
        res += tmp
        heapq.heappush(heap, tmp)
    print(res)


if __name__ == "__main__":
    main()
