# BOJ_2312
# 수 복원하기

import sys


def solution():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        res = {}

        div_num = 2
        while n != 1:
            if n % div_num == 0:
                if div_num not in res:
                    res[div_num] = 1
                else:
                    res[div_num] += 1
                n //= div_num
            else:
                div_num += 1
        for i in res.items():
            print(*i)


if __name__ == "__main__":
    solution()
