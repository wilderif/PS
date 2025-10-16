# 예상_대진표


def solution(n, a, b):
    res = 0
    while a != b:
        res += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return res
