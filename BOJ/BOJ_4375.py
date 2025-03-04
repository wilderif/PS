# BOJ_4375
# 1

import sys

inp = sys.stdin.readline


def main():
    while True:
        try:
            n = int(inp())
            tmp = 1
            res = 1
            while tmp % n:
                tmp %= n
                tmp = tmp * 10 + 1
                res += 1
            print(res)
        except:
            break


if __name__ == "__main__":
    main()
