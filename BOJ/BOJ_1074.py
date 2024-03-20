# BOJ_1074
# Z

import sys


def devide(size, r, c):
    if size == 1:
        return 0
    
    half = size // 2
    if r < half and c < half:
        return devide(half, r, c)
    elif r < half and c >= half:
        return half * half + devide(half, r, c - half)
    elif r >= half and c < half:
        return half * half * 2 + devide(half, r - half, c)
    else:
        return half * half * 3 + devide(half, r - half, c - half)


def main():
    n, r, c = map(int, sys.stdin.readline().split())
    print(devide(2 ** n, r, c))


if __name__ == "__main__":
    main()
