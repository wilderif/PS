# N개의_최소공배수


import math


def solution(arr):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    res = 1
    for i in arr:
        res = lcm(res, i)

    return res
