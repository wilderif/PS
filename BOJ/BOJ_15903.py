# BOJ_15903
# 카드 합체 놀이

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = list(map(int, inp().split()))
    heapq.heapify(arr)
    while m:
        m -= 1
        tmp1 = heapq.heappop(arr)
        tmp2 = heapq.heappop(arr)
        heapq.heappush(arr, tmp1 + tmp2)
        heapq.heappush(arr, tmp1 + tmp2)
    print(sum(arr))


if __name__ == "__main__":
    main()
