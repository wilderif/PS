# BOJ_17413
# 단어 뒤집기 2

import sys


def solution():
    s = sys.stdin.readline().rstrip()

    res = ""
    tmp = ""
    flag = False
    for i in range(len(s)):
        if s[i] == '<':
            flag = True
        if flag:
            tmp += s[i]
            if s[i] == '>':
                flag = False
                res += tmp
                tmp = ""
        else:
            if s[i] == ' ':
                res += tmp + ' '
                tmp = ""
            else:
                tmp = s[i] + tmp
    res += tmp

    print(res)
    

if __name__ == "__main__":
    solution()
