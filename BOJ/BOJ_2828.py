# BOJ_2828
# 사과 담기 게임

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    j = int(inp())
    arr = [int(inp()) for _ in range(j)]
    b_left = 1
    b_right = m

    res = 0
    for i in arr:
        if i < b_left:
            res += b_left - i
            b_left = i
            b_right = b_left + m - 1
        elif i > b_right:
            res += i - b_right
            b_right = i
            b_left = b_right - m + 1
    print(res)


if __name__ == "__main__":
    main()
