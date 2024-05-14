# BOJ_1018
# 체스판 다시 칠하기

import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = [sys.stdin.readline().rstrip() for _ in range(n)]
    
    res = 8 * 8 + 1
    for j in range(n - 8 + 1):
        for i in range(m - 8 + 1):
            res_1 = 0
            res_2 = 0
            for x in range(j, j + 8):
                for y in range(i, i + 8):
                    if (x + y) % 2:
                        if arr[x][y] == 'B':
                            res_1 += 1
                        else:
                            res_2 += 1
                    else:
                        if arr[x][y] == 'B':
                            res_2 += 1
                        else:
                            res_1 += 1
            res = min(res, res_1, res_2)
    print(res)


if __name__ == "__main__":
    main()
