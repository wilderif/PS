# BOJ_22862
# 가장 긴 짝수 연속한 부분 수열 (large)

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    idx_1, idx_2 = 0, 0
    res = 0
    cur_sequence = (arr[0] + 1) % 2
    cur_erase = arr[0] % 2
    while idx_2 < n:
        if cur_erase <= k:
            idx_2 += 1
            if idx_2 == n:
                break
            if arr[idx_2] % 2:
                cur_erase += 1
            else:
                cur_sequence += 1
        res = max(res, cur_sequence)
        if cur_erase > k:
            if idx_1 < idx_2:
                if arr[idx_1] % 2:
                    cur_erase -= 1
                else:
                    cur_sequence -= 1
                idx_1 += 1
    res = max(res, cur_sequence)
    print(res)


if __name__ == "__main__":
    main()
