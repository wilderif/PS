# BOJ_11000
# 강의실 배정

import sys


def main():
    n = int(sys.stdin.readline())
    arr = list()
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((a, 1))
        arr.append((b, -1))
    arr.sort(key=lambda x:(x[0], -x[1]))
    res, cur, idx, time = 0, 0, 0, 0
    while idx < n * 2:
        time = arr[idx][0]
        while idx < n * 2 and time == arr[idx][0]:
            cur += arr[idx][1]
            idx += 1
        res = max(res, cur)
    print(res)


if __name__ == "__main__":
    main()
