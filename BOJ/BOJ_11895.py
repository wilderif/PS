# BOJ_11895
# 속이기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    tmp = arr[0]
    for val in arr[1:]:
        tmp ^= val

    if tmp != 0:
        print(0)
        return

    arr.sort()
    print(sum(arr) - arr[0])


if __name__ == "__main__":
    main()
