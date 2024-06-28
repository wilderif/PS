# BOJ_24417
# 알고리즘 수업 - 피보나치 수 2

import sys

inp = sys.stdin.readline


def fibonacci(n):
    global cnt
    tmp1 = 1
    tmp2 = 1
    nxt = 0
    for i in range(3, n + 1):
        cnt += 1
        nxt = tmp1 + tmp2
        nxt %= 1000000007
        tmp1 = tmp2
        tmp2 = nxt
    return nxt


def main():
    global cnt
    n = int(inp())
    cnt = 0
    tmp = fibonacci(n)
    print(tmp, cnt)
            

if __name__ == "__main__":
    main()