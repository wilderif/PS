# BOJ_7662
# 이중 우선순위 큐

import sys
import heapq

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        k = int(inp())
        min_heap = []
        max_heap = []
        vis = [False for _ in range(1000000)]
        for key in range(k):    
            inst, num = inp().split()
            num = int(num)

            if inst == 'I':
                heapq.heappush(min_heap, (num, key))
                heapq.heappush(max_heap, (-num, key))
                vis[key] = True
            else:
                if num == 1:
                    if max_heap:
                        vis[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                else:
                    if min_heap:
                        vis[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
            while min_heap and not vis[min_heap[0][1]]:
                heapq.heappop(min_heap)
            while max_heap and not vis[max_heap[0][1]]:
                heapq.heappop(max_heap)
        if max_heap and min_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")


if __name__ == "__main__":
    main()
