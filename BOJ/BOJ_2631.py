# BOJ_2631
# 줄세우기

import sys


def main():
    n = int(sys.stdin.readline())
    arr = list()
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    mem = [1 for _ in range(n)]
    lis = 0
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                mem[i] = max(mem[i], mem[j] + 1)
        lis = max(lis, mem[i])

    print(n - lis)


if __name__ == "__main__":
    main()
