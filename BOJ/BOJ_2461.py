# BOJ_2461
# 대표 선수

import sys
import heapq

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = [sorted(list(map(int, inp().split())), reverse=True) for _ in range(n)]
    sel = [(arr[i].pop(), i) for i in range(n)]    
    heapq.heapify(sel)

    cur_min = sel[0][0]
    cur_max = 0
    for i in range(n):
        cur_max = max(cur_max, sel[i][0])
    res = cur_max - cur_min
    while True:
        target_idx = sel[0][1]
        if arr[target_idx]:
            cur_max = max(cur_max, arr[target_idx][-1])
            heapq.heappop(sel)
            heapq.heappush(sel, (arr[target_idx].pop(), target_idx))
            cur_min = sel[0][0]
        else:
            break
        res = min(res, cur_max - cur_min)
    print(res)


if __name__ == "__main__":
    main()
