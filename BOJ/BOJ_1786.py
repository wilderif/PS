# BOJ_1786
# 찾기

import sys

inp = sys.stdin.readline


def failure(s):
    f = [0 for _ in range(len(s))]
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
        f[i] = j
    return f


def main():
    t = inp().rstrip()
    p = inp().rstrip()
 
    res_1 = 0
    res_2 = []    
    f = failure(p)
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = f[j - 1]
        if t[i] == p[j]:
            j += 1
        if j == len(p):
            res_1 += 1
            res_2.append(i - len(p) + 2)
            j = f[j - 1]
    print(res_1)
    print(*res_2)


if __name__ == "__main__":
    main()
