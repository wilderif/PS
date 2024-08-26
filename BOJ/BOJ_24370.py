# BOJ_24370
# 알고리즘 수업 - 점근적 표기 6

import sys

inp = sys.stdin.readline


def main():
    a2, a1, a0 = map(int, inp().split())
    c1, c2 = map(int, inp().split())
    n = int(inp())

    if a2 < c1:
        print(0)
        return
    elif a2 == c1:
        if -a1 * n - a0 > 0:
            print(0)
            return
        elif -a1 * n - a0 == 0:
            if -a1 * (n + 1) - a0 > 0:
                print(0)
                return
    else:
        v = a1 / (2 * (c1 - a2))
        if v <= n:
            if (c1 - a2) * n ** 2 - a1 * n - a0 > 0:
                print(0)
                return
        else:
            if (c1 - a2) * v ** 2 - a1 * v - a0 > 0:
                print(0)
                return
                
    if a2 > c2:
        print(0)
        return
    elif a2 == c2:
        if -a1 * n - a0 < 0:
            print(0)
            return
        elif -a1 * n - a0 == 0:
            if -a1 * (n + 1) - a0 < 0:
                print(0)
                return
    else:
        v = a1 / (2 * (c2 - a2))
        if v <= n:
            if (c2 - a2) * n ** 2 - a1 * n - a0 < 0:
                print(0)
                return
        else:
            if (c2 - a2) * v ** 2 - a1 * v - a0 < 0:
                print(0)
                return
    print(1)


if __name__ == "__main__":
    main()
