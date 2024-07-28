# BOJ_13417
# 카드 문자열

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = list(inp().split())
        res = arr[0]
        for i in range(1, n):
            if ord(arr[i]) <= ord(res[0]):
                res = arr[i] + res
            else:
                res = res + arr[i]
        print(res)


if __name__ == "__main__":
    main()
