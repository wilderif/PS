# BOJ_18311
# 왕복

import sys

inp = sys.stdin.readline


def main():
    n, k = map(int, inp().split())
    arr = list(map(int, inp().split()))
    total = sum(arr)
    for idx, val in enumerate(arr):
        if k < val:
            print(idx + 1)
            return
        k -= val
    for idx, val in enumerate(reversed(arr)):
        if k < val:
            print(n - idx)
            return
        k -= val


if __name__ == "__main__":
    main()
