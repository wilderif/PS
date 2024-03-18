# BOJ_2473
# 세 용액

import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    res = None
    minimum = int(1e9 * 3 + 1)
    for i in range(n - 2):        
        idx_l = i + 1
        idx_r = n - 1
        while True:
            if idx_l == idx_r:
                break

            cur = arr[i] + arr[idx_l] + arr[idx_r]
            if cur < 0:
                cur = -cur
                if cur < minimum:
                    minimum = cur
                    res = [arr[i], arr[idx_l], arr[idx_r]]
                idx_l += 1
            elif cur == 0:
                res = [arr[i], arr[idx_l], arr[idx_r]]
                print(*res)
                return None
            elif cur > 0:
                if cur < minimum:
                    minimum = cur
                    res = [arr[i], arr[idx_l], arr[idx_r]]
                idx_r -= 1

    print(*res)


if __name__ == "__main__":
    main()
