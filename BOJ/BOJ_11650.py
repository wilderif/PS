# BOJ_11650
# 좌표 정렬하기

import sys


def merge(arr, start, end):
    mid = (start + end) // 2
    idx_1 = start
    idx_2 = mid
    tmp = list()
    for _ in range(end - start):
        if idx_1 == mid:
            tmp.append(arr[idx_2])
            idx_2 += 1
        elif idx_2 == end:
            tmp.append(arr[idx_1])
            idx_1 += 1
        elif arr[idx_1][0] != arr[idx_2][0]:
            if arr[idx_1][0] <= arr[idx_2][0]:
                tmp.append(arr[idx_1])
                idx_1 += 1
            else:
                tmp.append(arr[idx_2])
                idx_2 += 1
        else:
            if arr[idx_1][1] <= arr[idx_2][1]:
                tmp.append(arr[idx_1])
                idx_1 += 1
            else:
                tmp.append(arr[idx_2])
                idx_2 += 1
            
    for i in range(end - start):
        arr[start + i] = tmp[i]


def merge_sort(arr, start, end):
    if start + 1 == end:
        return None
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, end)


def main():
    n = int(sys.stdin.readline())
    arr = list()
    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        arr.append(tmp)
    
    merge_sort(arr, 0, n)
    for i in arr:
        print(*i)

    
if __name__ == "__main__":
    main()
