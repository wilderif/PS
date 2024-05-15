# BOJ_1120
# 문자열

import sys

inp = sys.stdin.readline


def main():
    a, b = inp().split()
    cnt = 0
    for i in range(len(b) - len(a) + 1):
        tmp = 0
        for j in range(len(a)):
            if a[j] == b[i + j]:
                tmp += 1
        cnt = max(cnt, tmp)
    print(len(a) - cnt)


if __name__ == "__main__":
    main()
