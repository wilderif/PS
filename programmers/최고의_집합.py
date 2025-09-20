# 최고의_집합


def solution(n, s):
    if n > s:
        return [-1]

    base = s // n
    remain = s % n

    res = [base for _ in range(n)]
    for i in range(remain):
        idx = n - 1 - i
        res[idx] += 1

    return res
