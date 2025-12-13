# 행렬의_곱셈


def solution(arr1, arr2):
    r_1, c_1 = len(arr1), len(arr1[0])
    r_2, c_2 = len(arr2), len(arr2[0])

    res = [[0 for _ in range(c_2)] for _ in range(r_1)]

    for i in range(r_1):
        for j in range(c_2):
            for k in range(c_1):
                res[i][j] += arr1[i][k] * arr2[k][j]

    return res
