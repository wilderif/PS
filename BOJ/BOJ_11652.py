# BOJ_11652
# 카드

import sys


def main():
    n = int(input())
    arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
    cur_max = 0
    cur_strick = 1
    cur_max_val = arr[0]

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            cur_strick += 1
        else:
            if cur_strick > cur_max:
                cur_max = cur_strick
                cur_max_val = arr[i - 1]
            cur_strick = 1

        if i == n - 1:
            if cur_strick > cur_max:
                cur_max = cur_strick
                cur_max_val = arr[i]

    print(cur_max_val)

    
if __name__ == "__main__":
    main()
