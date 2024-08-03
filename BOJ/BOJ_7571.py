# BOJ_7571
# 점 모으기

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr_1 = []
    arr_2 = []
    for _ in range(m):
        a, b = map(int, inp().split())
        arr_1.append(a)
        arr_2.append(b)
    arr_1.sort()
    arr_2.sort()

    mid_1 = arr_1[m // 2]
    mid_2 = arr_2[m // 2]
    
    res = 0
    for i in range(m):
        res += abs(arr_1[i] - mid_1)
        res += abs(arr_2[i] - mid_2)
    print(res)


if __name__ == "__main__":
    main()
