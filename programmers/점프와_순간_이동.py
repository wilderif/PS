# 점프와_순간_이동


def solution(n):
    res = 0
    while n != 0:
        if n % 2:
            res += 1
            n -= 1
        else:
            n //= 2

    return res
