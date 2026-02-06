# BOJ_14746
# Closest Pair

import sys
import bisect

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    c1, c2 = map(int, inp().split())
    arr1 = sorted(list(map(int, inp().split())))
    arr2 = sorted(list(map(int, inp().split())))

    res1 = 2 * int(1e8)
    res2 = 0
    for i in arr1:
        idx_l = bisect.bisect_left(arr2, i)
        tmp = []
        if idx_l - 1 >= 0:
            tmp.append(abs(i - arr2[idx_l - 1]))
        if idx_l < m:
            tmp.append(abs(i - arr2[idx_l]))

        for tmp_min in tmp:
            if tmp_min < res1:
                res1 = tmp_min
                res2 = 1
            elif tmp_min == res1:
                res2 += 1

    print(res1 + abs(c1 - c2), res2)


if __name__ == "__main__":
    main()
