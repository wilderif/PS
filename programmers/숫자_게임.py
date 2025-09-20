# 숫자_게임


def solution(A, B):
    size = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    idx_1 = 0
    idx_2 = 0

    res = 0
    while idx_1 < size and idx_2 < size:
        if A[idx_1] < B[idx_2]:
            res += 1
            idx_2 += 1
        idx_1 += 1

    return res
