# BOJ_9237
# 이장님 초대

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    arr.sort(reverse=True)
    res = 0
    for i in range(n):
        res = max(res, arr[i] + i + 1)
    print(res + 1)


if __name__ == "__main__":
    main()
