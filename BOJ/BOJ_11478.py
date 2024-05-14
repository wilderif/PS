# BOJ_11478
# 서로 다른 부분 문자열의 개수

import sys


def solution():
    s = list(sys.stdin.readline().rstrip())
    res = set()

    for i in range(len(s)):
        new = s[i]
        if new not in res:
            res.add(new)
        for j in range(i + 1, len(s)):
            new += s[j]
            if new not in res:
                res.add(new)
    print(len(res))


if __name__ == "__main__":
    solution()
