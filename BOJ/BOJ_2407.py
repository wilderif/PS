# BOJ_2407
# 조합

def solution():
    n, m = map(int, input().split())

    res_1 = 1
    res_2 = 1

    for i in range(n, n - m, -1):
        res_1 = res_1 * i
        res_2 = res_2 * (n - i + 1)
    print(res_1 // res_2)


if __name__ == "__main__":
    solution()
