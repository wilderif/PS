# BOJ_21557
# 불꽃놀이

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    l, r = arr[0], arr[-1]
    for _ in range(n - 3):
        if l <= r:
            r -= 1
        else:
            l -= 1
    else:
        r -= 1
        l -= 1
    print(max(l, r))


if __name__ == "__main__":
    main()
