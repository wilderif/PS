# BOJ_1351
# 무한 수열

import sys

inp = sys.stdin.readline


def recursion(n):
    if n in dic:
        return dic[n]
    dic[n] = recursion(n // p) + recursion(n // q)
    return dic[n]


def main():
    global dic, p, q
    n, p, q = map(int, inp().split())
    dic = {}
    dic[0] = 1
    print(recursion(n))


if __name__ == "__main__":
    main()
