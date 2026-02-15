# BOJ_1740
# 거듭제곱

import sys

inp = sys.stdin.readline


def main():
    n = bin(int(inp()))[2:][::-1]
    res = 0
    tmp = 1
    for i in n:
        if i == "1":
            res += tmp
        tmp *= 3
    print(res)


if __name__ == "__main__":
    main()
