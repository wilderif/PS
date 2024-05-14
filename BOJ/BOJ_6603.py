# BOJ_6603
# 로또

import sys


def backtracking(idx, arr, arr_out, used):
    if idx == 6:
        for i in range(6):
            print(arr[arr_out[i]], end=' ')
        print()
    else:
        start = 1
        if idx:
            start = arr_out[idx - 1]
        for i in range(start, k + 1):
            if not used[i]:
                arr_out[idx] = i
                used[i] = True
                backtracking(idx + 1, arr, arr_out, used)
                used[i] = False


def main():
    while True:
        arr = list(map(int, sys.stdin.readline().split()))
        if arr[0] == 0:
            break
        global k
        k = arr[0]
        arr_out = [0 for _ in range(6)]
        used = [False for _ in range(k + 1)]
        backtracking(0, arr, arr_out, used)
        print()


if __name__ == "__main__":
    main()
