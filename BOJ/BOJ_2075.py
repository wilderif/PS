# BOJ_2075
# N번째 큰 수

import sys
import heapq

inp = sys.stdin.readline


def main():
    # n = int(inp())
    # arr = [list(map(int, inp().split())) for _ in range(n)]
    # max_heap = []
    # for i in range(n):
    #     heapq.heappush(max_heap, (-arr[n - 1][i], i, n - 1))
    # n -= 1
    # while n:
    #     tmp = heapq.heappop(max_heap)
    #     if tmp[2]:
    #         heapq.heappush(max_heap, (-arr[tmp[2] - 1][tmp[1]], tmp[1], tmp[2] - 1))
    #     n -= 1
    # print(-max_heap[0][0])

    n = int(inp())
    min_heap = [-float("inf")]
    for _ in range(n):
        for i in map(int, inp().split()):
            if i > min_heap[0]:
                heapq.heappush(min_heap, i)
                if len(min_heap) > n:
                    heapq.heappop(min_heap)
    print(min_heap[0])

                
if __name__ == "__main__":
    main()
