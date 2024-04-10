# BOJ_24313
# 알고리즘 수업 - 점근적 표기 1

import sys


def main():
    a1, a0 = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.readline())
    n0 = int(sys.stdin.readline())

    print(1) if c * n0 >= a1 * n0 + a0 and a1 <= c else print(0)


if __name__ == "__main__":
    main()
