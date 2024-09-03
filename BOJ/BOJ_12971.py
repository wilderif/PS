# BOJ_12971
# 숫자 놀이

import sys

inp = sys.stdin.readline


def main():
    p1, p2, p3, x1, x2, x3 = map(int, inp().split())
    if x1 >= p1 or x2 >= p2 or x3 >= p3:
        return -1
    for i in range(1, 27000001):
        if i % p1 == x1 and i % p2 == x2 and i % p3 == x3:
            print(i)
            return
    else:
        print(-1)


if __name__ == "__main__":
    main()
