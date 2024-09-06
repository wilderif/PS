# BOJ_14241
# 슬라임 합치기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    arr.sort()
    res = 0

    while len(arr) > 1:
        tmp1 = arr.pop()
        tmp2 = arr.pop()
        res += tmp1 * tmp2
        arr.append(tmp1 + tmp2)
    print(res)


if __name__ == "__main__":
    main()
