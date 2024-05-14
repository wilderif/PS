# BOJ_12015
# 가장 긴 증가하는 부분 수열 2

import sys


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


def main():
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    res = [arr[0]]
    for i in range(1, n):
        if res[-1] < arr[i]:
            res.append(arr[i])
        elif res[-1] > arr[i]:
            res[binary_search(res, arr[i])] = arr[i]
    print(len(res))


if __name__ == "__main__":
    main()
