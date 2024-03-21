# BOJ_11729
# 하노이 탑 이동 순서

import sys
sys.setrecursionlimit(int(1e9))


def devide(size, start, end):
    if size == 1:
        print(start, end)
        return None

    devide(size - 1, start, 6 - start - end)
    print(start, end)
    devide(size - 1, 6 - start - end, end)


def main():
    n = int(input())
    print(2 ** n - 1)
    devide(n, 1, 3)


if __name__ == "__main__":
    main()
