# BOJ_10816
# 숫자 카드 2

import sys


def binary_search(arr, target):
    start = 0
    end = len(arr)
    lower, upper = 0, 0
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    lower = start

    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    upper = end
    
    return upper - lower


def main():
    n = int(input())
    arr_1 = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    arr_2 = list(map(int, sys.stdin.readline().split()))
    arr_1.sort()

    for i in arr_2:
        print(binary_search(arr_1, i), end=' ')
    

if __name__ == "__main__":
    main()
