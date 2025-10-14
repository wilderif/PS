# 카펫


import math


def solution(brown, yellow):
    def check(x, y):
        nonlocal res
        if (x + 1) * 2 + (y + 1) * 2 == brown:
            res[0] = y + 2
            res[1] = x + 2
            return True
        return False

    res = [0, 0]
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if not yellow % i:
            if check(i, yellow // i):
                return res
