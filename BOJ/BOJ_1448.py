# BOJ_1448
# 삼각형 만들기

import sys


def solution():
    n = int(input())
    line = []
    for _ in range(n):
        line.append(int(sys.stdin.readline()))
    line.sort(reverse=True)

    for i in range(n - 2):
        if line[i] < line[i + 1] + line[i + 2]:
            print(line[i] + line[i + 1] + line[i + 2])
            break
    else:
        print(-1)


if __name__ == "__main__":
    solution()
