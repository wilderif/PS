# BOJ_6137
# 문자열 생성

import sys


def solution():
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(sys.stdin.readline().strip())
    
    res = ""
    idx_l = 0
    idx_r = len(arr) - 1
    while idx_l <= idx_r:
        if arr[idx_l] < arr[idx_r]:
            res += arr[idx_l]
            idx_l += 1
        elif arr[idx_l] == arr[idx_r]:
            tmp_l, tmp_r = idx_l, idx_r
            while True:
                if tmp_r <= tmp_l:
                    res += arr[idx_l]
                    idx_l += 1
                    break
                if arr[tmp_l] < arr[tmp_r]:
                    res += arr[idx_l]
                    idx_l += 1
                    break
                elif arr[tmp_l] == arr[tmp_r]:
                    tmp_l += 1
                    tmp_r -= 1
                else:
                    res += arr[idx_r]
                    idx_r -= 1
                    break
        else:
            res += arr[idx_r]
            idx_r -= 1
    for i in range(len(res)):
        print(res[i], end='')
        if not ((i + 1) % 80):
            print()


if __name__ == "__main__":
    solution()
