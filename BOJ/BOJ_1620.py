# BOJ_1620
# 나는야 포켓몬 마스터 이다솜

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    dic_1 = {}
    dic_2 = {}
    for i in range(1, n + 1):
        a = sys.stdin.readline().rstrip()
        dic_1[a] = i
        dic_2[i] = a

    for _ in range(m):
        a = sys.stdin.readline().rstrip()
        if a in dic_1.keys():
            print(dic_1[a])
        else:
            print(dic_2[int(a)])


if __name__ == "__main__":
    solution()
