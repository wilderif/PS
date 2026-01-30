# BOJ_5545
# 최고의 피자

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    a, b = map(int, inp().split())
    c = int(inp())
    arr = sorted([int(inp()) for _ in range(n)], reverse=True)
    cur_cal = c
    cur_price = a
    cur_max = cur_cal / cur_price
    for i in range(n):
        cur_cal += arr[i]
        cur_price += b
        if cur_cal / cur_price > cur_max:
            cur_max = cur_cal / cur_price
        else:
            break
    print(int(cur_max))


if __name__ == "__main__":
    main()
