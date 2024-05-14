# BOJ_2143
# 두 배열의 합

import sys
import bisect


def main():
    t = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    n_arr = [int(i) for i in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    m_arr = [int(i) for i in sys.stdin.readline().split()]

    arr_1 = []
    arr_2 = []
    for i in range(n):
        prefix = n_arr[i]
        arr_1.append(prefix)
        for j in range(i + 1, n):
            prefix += n_arr[j]
            arr_1.append(prefix)
    for i in range(m):
        prefix = m_arr[i]
        arr_2.append(prefix)
        for j in range(i + 1, m):
            prefix += m_arr[j]
            arr_2.append(prefix)
    arr_1.sort()
    arr_2.sort()

    res = 0
    for i in range(len(arr_1)):
        target = t - arr_1[i]
        idx_1 = bisect.bisect_left(arr_2, target)
        idx_2 = bisect.bisect_right(arr_2, target)
        res += idx_2 - idx_1
    print(res)


if __name__ == "__main__":
    main()
