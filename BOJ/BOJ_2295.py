# BOJ_2295
# 세 수의 합

import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    arr = list(int(sys.stdin.readline()) for _ in range(n))
    arr.sort()
    arr_2 = list()
    for i in range(n):
        for j in range(i, n):
            arr_2.append(arr[i] + arr[j])
    arr_2.sort()
    res = 0
    for i in range(n):
        for j in range(n):
            if arr[i] - arr[j] >= 0:
                idx = bisect.bisect_left(arr_2, arr[i] - arr[j])
                if arr_2[idx] == arr[i] - arr[j]:
                    res = max(res, arr[i])
    print(res)


if __name__ == "__main__":
    main()
