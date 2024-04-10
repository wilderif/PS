# BOJ_2283
# 구간 자르기

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    max_range = 1000001
    arr = [0 for _ in range(max_range)]
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().split())
        arr[s] += 1
        arr[e] -= 1
    for i in range(1, max_range):
        arr[i] += arr[i - 1]

    idx_1, idx_2 = 0, 0
    cur = 0
    while idx_2 < max_range:
        if cur < k:
            cur += arr[idx_2]
            idx_2 += 1
        elif cur == k:
            print(idx_1, idx_2)
            return None
        else:
            cur -= arr[idx_1]
            idx_1 += 1
    print(0, 0)


if __name__ == "__main__":
    main()
