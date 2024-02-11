# BOJ_1769
# 3의 배수

import sys


def solution():
    x = list(map(int, sys.stdin.readline().strip()))

    cnt = 0
    while len(x) >= 2:
        cnt += 1
        tmp = 0

        for i in x:
            tmp += i
        
        x = list(map(int, str(tmp)))

    print(cnt)

    if (x[0] % 3):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    solution()
