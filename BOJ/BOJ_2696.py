# BOJ_2696
# 중앙값 구하기

import sys
import heapq

inp = sys.stdin.readline


def solution():
    m = int(inp())
    arr = []
    for _ in range((m + 9) // 10):
        arr.extend(list(map(int, inp().split())))
    ret = []
    max_heap = []
    min_heap = []

    for i in range(m):
        num = arr[i]
        if len(min_heap) == len(max_heap):
            if not max_heap:
                heapq.heappush(max_heap, -num)
            else:
                if num <= min_heap[0]:
                    heapq.heappush(max_heap, -num)
                elif min_heap[0] < num:
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                    heapq.heappush(min_heap, num)
            ret.append(-max_heap[0])
        else:
            if num <= -max_heap[0]:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

    return ret


def main():
    t = int(inp())
    for _ in range(t):
        ret = solution()
        print(len(ret))
        for i in range(len(ret)):
            print(ret[i], end=" ")
            if (i + 1) % 10 == 0:
                print()


if __name__ == "__main__":
    main()
