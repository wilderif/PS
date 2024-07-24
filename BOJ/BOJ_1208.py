# BOJ_1208
# 부분수열의 합 2

import sys
from itertools import combinations

inp = sys.stdin.readline


def find_sum(arr):
    ret = {}
    for i in range(1, len(arr) + 1):
        for com in combinations(arr, i):
            tmp = sum(com)
            if tmp in ret:
                ret[tmp] += 1
            else:
                ret[tmp] = 1
    return ret


def main():
    n, s = map(int, inp().split())
    arr = list(map(int, inp().split()))

    sum1 = find_sum(arr[:n // 2])
    sum2 = find_sum(arr[n//2:])

    res = 0
    if s in sum1:
        res += sum1[s]
    if s in sum2:
        res += sum2[s]

    for i in sum1:
        if s - i in sum2:
            res += sum1[i] * sum2[s - i]

    print(res)


if __name__ == "__main__":
    main()
