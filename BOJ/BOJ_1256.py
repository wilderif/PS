# BOJ_1256
# 사전

import sys

inp = sys.stdin.readline


def combination(n, r):
    if r > n - r:
        r = n - r
    ret = 1
    for i in range(r):
        ret = (ret * (n - i)) // (i + 1)

    return int(ret)


def solution(len_total, len_a, len_z, target):
    global res
    if not len_total:
        return
    
    if not len_z:
        res += "a" * len_a
        return
    elif not len_a:
        res += "z" * len_z
        return
    
    comb = combination(len_total - 1, len_a - 1)
    if comb >= target:
        res += "a"
        solution(len_total - 1, len_a - 1, len_z, target)
    else:
        res += "z"
        solution(len_total - 1, len_a, len_z - 1, target - comb)


def main():
    global res
    n, m, k = map(int, inp().split())
    
    res = ""
    if combination(n + m , n) < k:
        print(-1)
        return
    
    solution(n + m, n, m, k)
    print(res)


if __name__ == "__main__":
    main()
