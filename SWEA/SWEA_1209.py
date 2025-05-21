# SWEA_1209
# [S/W 문제해결 기본] 2일차 - Sum


for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    res = 0
    digonal1 = 0
    digonal2 = 0

    for i in range(100):
        digonal1 += arr[i][i]
        digonal2 += arr[i][100 - 1 - i]
        tmp1 = sum(arr[i])
        tmp2 = 0
        for j in range(100):
            tmp2 += arr[j][i]

        res = max(res, tmp1, tmp2)
    res = max(res, digonal1, digonal2)

    print(f"#{test_case} {res}")
