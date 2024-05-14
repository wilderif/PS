# BOJ_1021
# 회전하는 큐

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = deque(i + 1 for i in range(n))
    target = list(map(int, inp().split()))
    cnt = 0
    for i in range(m):
        target_idx = arr.index(target[i])
        if target_idx > len(arr) // 2:
            for _ in range(len(arr) - target_idx):
                arr.appendleft(arr.pop())
                cnt += 1
        else:
            for _ in range(target_idx):
                arr.append(arr.popleft())
                cnt += 1
        arr.popleft()
    print(cnt)


if __name__ == "__main__":
    main()
