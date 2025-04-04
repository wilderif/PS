# BOJ_2481
# 해밍 경로

import sys
from collections import deque

inp = sys.stdin.readline


def find_prev():
    q = deque()
    prev = [-1 for _ in range(n + 1)]

    q.append(1)
    prev[1] = 0

    while q:
        cur = q.popleft()
        cur_val = codes[cur]
        for i in range(k):
            nxt_val = cur_val ^ (1 << i)
            if nxt_val in index and prev[index[nxt_val]] == -1:
                q.append(index[nxt_val])
                prev[index[nxt_val]] = cur

    return prev


def find_path(prev, dst):
    if prev[dst] == -1:
        return [-1]

    cur_node = dst
    path = deque()
    while cur_node:
        path.appendleft(cur_node)
        cur_node = prev[cur_node]

    return path


def main():
    global n, k, codes, index
    n, k = map(int, inp().split())

    codes = {}
    index = {}

    for i in range(1, n + 1):
        num = int(inp(), 2)
        index[num] = i
        codes[i] = num

    prev = find_prev()

    m = int(inp())
    for _ in range(m):
        dst = int(inp())
        print(*find_path(prev, dst))


if __name__ == "__main__":
    main()
