# BOJ_7568
# 덩치

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    res = []
    for i in range(n):
        tmp = 1
        for j in range(n):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                tmp += 1
        res.append(tmp)
    print(*res)


if __name__ == "__main__":
    main()
