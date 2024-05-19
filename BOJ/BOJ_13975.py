# BOJ_13975
# 파일 합치기 3

import sys
import heapq

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        heap = list(map(int, inp().split()))
        heapq.heapify(heap)
        res = 0
        while len(heap) > 1:
            tmp = heapq.heappop(heap) + heapq.heappop(heap)
            res += tmp
            heapq.heappush(heap, tmp)
        else:
            print(res)

    
if __name__ == "__main__":
    main()
