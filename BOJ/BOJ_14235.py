# BOJ_14235
# 크리스마스 선물

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    max_heap = []
    for _ in range(n):
        tmp = list(map(int, inp().split()))
        for i in range(tmp[0]):
            heapq.heappush(max_heap, -tmp[i + 1])
        if tmp[0]:
            continue
        if not max_heap:
            print(-1)
        else:
            print(-heapq.heappop(max_heap))

                
if __name__ == "__main__":
    main()
