# BOJ_35144
# E99

import sys

inp = sys.stdin.readline


def main():
    a, b = map(int, inp().split())
    if a == b:
        print("INF")
        return
    elif b > a:
        a, b = b, a

    res1, res2 = b**2, (a - b)
    for i in range(2, (a - b) + 1):
        if i > res2:
            break
        while res1 % i == 0 and res2 % i == 0:
            res1 //= i
            res2 //= i

    print(res1, res2)


if __name__ == "__main__":
    main()
