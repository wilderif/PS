# BOJ_29700
# 우당탕탕 영화예매

import sys


def solution():
    n, m, k = map(int, sys.stdin.readline().split())
    theater = list()

    for _ in range(n):
        theater.append(sys.stdin.readline().strip())

    res = 0
    for s in theater:
        strick = 0
        for i in range(len(s)):
            if s[i] == '0':
                strick += 1
            if s[i] == '1' or i == len(s) - 1:
                if strick >= k:
                    res += strick - k + 1
                strick = 0

    print(res)
            

if __name__ == "__main__":
    solution()
