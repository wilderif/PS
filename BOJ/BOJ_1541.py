# BOJ_1541
# 잃어버린 괄호

import sys


def solution():
    string = sys.stdin.readline().rstrip()
    parsing = []
    idx = 0
    for i in range(len(string)):
        if string[i] == '-' or string[i] == '+':
            parsing.append(int(string[idx:i]))
            parsing.append(string[i])
            idx = i + 1
    else:
        parsing.append(int(string[idx:]))

    res = parsing[0]
    if '-' in parsing:
        minus_idx = 0
        for i in range(len(parsing)):
            if parsing[i] == '-':
                minus_idx = i
                break
        for i in range(2, minus_idx, 2):
            res += parsing[i]
        for i in range(minus_idx + 1, len(parsing), 2):
            res -= parsing[i]
    else:
        for i in range(2, len(parsing), 2):
            res += parsing[i]
    print(res)


if __name__ == "__main__":
    solution()
