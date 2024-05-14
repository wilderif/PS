# BOJ_1051
# 숫자 정사각형

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = [list(inp().rstrip()) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            tmp = res
            while i + tmp < n and j + tmp < m:
                if arr[i][j + tmp] == arr[i][j] and arr[i + tmp][j]  == arr[i][j] and arr[i + tmp][j + tmp] == arr[i][j]:
                    res = max(res, tmp)
                tmp += 1
    print((res + 1) ** 2)


if __name__ == "__main__":
    main()
