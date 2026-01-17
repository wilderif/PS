# BOJ_28324
# 스케이트 연습

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    cur_max = 1

    for i in range(n - 1, -1, -1):
        if arr[i] > cur_max:
            arr[i] = cur_max
        else:
            cur_max = arr[i]
        cur_max += 1

    print(sum(arr))


if __name__ == "__main__":
    main()
