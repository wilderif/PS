# BOJ_1920
# 수 찾기

import sys


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] == target:
            return 1
        else:
            start = mid + 1
    else:
        return 0


def main():
    n = int(input())
    arr_1 = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    arr_2 = list(map(int, sys.stdin.readline().split()))
    arr_1.sort()

    for i in arr_2:
        print(binary_search(arr_1, i))
    

if __name__ == "__main__":
    main()
