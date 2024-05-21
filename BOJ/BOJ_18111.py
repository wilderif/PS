# BOJ_18111
# 마인크래프트

import sys

inp = sys.stdin.readline


def main():
    n, m, b = map(int, inp().split())
    arr = [0] * 257
    for _ in range(n):
        for i in map(int, inp().split()):
            arr[i] += 1
    res_time = 500 * 500 * 256 * 2
    res_height = 0
    for i in range(257):
        tmp_time = 0
        tmp_b = b
        for j in range(257):
            if j >= i:
                tmp_time += 2 * (j - i) * arr[j]
                tmp_b += (j - i) * arr[j]
            else:
                tmp_time += (i - j) * arr[j]
                tmp_b -= (i - j) * arr[j]
        if tmp_b >= 0:
            if tmp_time <= res_time:
                res_time = tmp_time
                res_height = i
    print(res_time, res_height)

    
if __name__ == "__main__":
    main()
