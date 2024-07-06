# BOJ_1300
# K번째 수

import sys

inp = sys.stdin.readline


def check(target):
    ret = 0
    for i in range(1, n + 1):
        ret += min(n, target // i)
    return ret < k


def binary_search():
    start = 1
    end = n * n
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            start = mid + 1
        else:
            end = mid - 1
    return start


def main():
    global n, k
    n = int(inp())
    k = int(inp())
    print(binary_search())


if __name__ == "__main__":
    main()
