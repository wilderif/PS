# BOJ_2437
# 저울

import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    cur_end = 0
    for i in arr:
        if i <= cur_end + 1:
            cur_end += i
        else:
            print(cur_end + 1)
            break
    else:
        print(sum(arr) + 1)


if __name__ == "__main__":
    main()
