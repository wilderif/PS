# BOJ_1654
# 랜선 자르기

import sys


def check(target):
    cur = 0
    for i in arr:
        cur += i // target
    return cur >= n


def search(start, end):
    while start < end:
        mid = (start + end + 1) // 2
        if check(mid):
            start = mid
        else:
            end = mid - 1
    return start


def main():
    global arr, n
    k, n = [int(x) for x in sys.stdin.readline().split()]
    arr = list(int(sys.stdin.readline()) for _ in range(k))
    print(search(1, max(arr)))
    

if __name__ == "__main__":
    main()
