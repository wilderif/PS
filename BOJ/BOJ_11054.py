# BOJ_11054
# 가장 긴 바이토닉 부분 수열

import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    mem_in = list(1 for _ in range(n))
    mem_de = list(1 for _ in range(n))
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                mem_in[i] = max(mem_in[i], mem_in[j] + 1)
            if arr[n - i - 1] > arr[n - j - 1]:
                mem_de[n - i - 1] = max(mem_de[n - i - 1], mem_de[n - j - 1] + 1)
    res = 0
    for i in range(n):
        res = max(res, mem_in[i] + mem_de[i] - 1)
    print(res)


if __name__ == "__main__":
    main()
