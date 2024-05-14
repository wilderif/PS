# BOJ_24061
# 알고리즘 수업 - 병합 정렬 2

import sys

inp = sys.stdin.readline


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    global cnt
    i = p
    j = q + 1
    t = 1
    tmp = [None for _ in range(r - p + 2)]
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t += 1
            i += 1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r:
        arr[i] = tmp[t]
        if cnt == k:
            print(*arr)
            sys.exit()
        cnt += 1
        i += 1
        t += 1


def main():
    global k, cnt
    n, k = map(int, inp().split())
    arr = list(map(int, inp().split()))
    cnt = 1
    merge_sort(arr, 0, n - 1)
    print(-1)


if __name__ == "__main__":
    main()
