# BOJ_17219
# 비밀번호 찾기

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    dic = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        dic[a] = b
    for _ in range(m):
        print(dic[sys.stdin.readline().rstrip()])


if __name__ == "__main__":
    solution()
