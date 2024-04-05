# BOJ_1456
# 거의 소수

import sys


def main():
    a, b = map(int, sys.stdin.readline().split())
    arr = [True for _ in range(int(b ** 0.5) + 1)]
    arr[0] = False
    arr[1] = False
    for i in range(len(arr)):
        if arr[i]:
            for j in range(2, len(arr)):
                if i * j >= len(arr):
                    break
                arr[i * j] = False
    res = 0
    for i in range(len(arr)):
        if arr[i]:
            tmp = i * i
            while tmp <= b:
                if tmp >= a:
                    res += 1
                tmp *= i
    print(res)


if __name__ == "__main__":
    main()
