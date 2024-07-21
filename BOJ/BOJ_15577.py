# BOJ_15577
# Prosjek

import sys
import heapq

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [int(inp()) for _ in range(n)]
    heapq.heapify(arr)
    for _ in range(n - 1):
        tmp1 = heapq.heappop(arr)
        tmp2 = heapq.heappop(arr)
        tmp = (tmp1 + tmp2) / 2
        heapq.heappush(arr, tmp)
    print(f"{arr[0]:.6f}")


if __name__ == "__main__":
    main()
