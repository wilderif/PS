# BOJ_5582
# 공통 부분 문자열

import sys

inp = sys.stdin.readline


def main():
    s1 = inp().strip()
    s2 = inp().strip()
    prev = [0 for _ in range(len(s2) + 1)]
    cur = [0 for _ in range(len(s2) + 1)]

    res = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                cur[j + 1] = prev[j] + 1
                res = max(res, cur[j + 1])
            else:
                cur[j + 1] = 0
        prev, cur = cur, prev

    print(res)

    
if __name__ == "__main__":
    main()
