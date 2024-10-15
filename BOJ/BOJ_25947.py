# BOJ_25947
# 선물할인

import sys

inp = sys.stdin.readline


def main():
    n, b, a = map(int, inp().split())
    arr = list(map(int, inp().split()))
    arr.sort()

    left = 0
    right = a - 1
    cur = 0
    for i in range(a):
        tmp = cur + arr[i] // 2
        if tmp > b:
            print(i)
            return
        cur = tmp

    while right < n - 1:
        tmp = cur + arr[right + 1] // 2 + arr[left] // 2
        if tmp > b:
            break
        left += 1
        right += 1
        cur = tmp
    print(right + 1)


if __name__ == "__main__":
    main()
