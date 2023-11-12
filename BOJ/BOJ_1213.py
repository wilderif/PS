# BOJ_1213
# 팰린드롬 만들기

import sys


def solution():
    s = list(sys.stdin.readline().rstrip())
    check = []
    res = [0 for _ in range(len(s))]

    s.sort()
    for i in s:
        if len(check) == 0:
            check.append([i, 1])
        elif check[-1][0] == i:
            check[-1][1] += 1
        else:
            check.append([i, 1])

    check_odd = 0
    odd_char = ''
    for i in check:
        if i[1] % 2 != 0:
            check_odd += 1
            odd_char = i[0]

        if check_odd == 2:
            print("I'm Sorry Hansoo")
            sys.exit()

    idx = 0

    for i in check:
        if i[0] != odd_char:
            for j in range(int(i[1] / 2)):
                res[idx] = i[0]
                res[len(res) - idx - 1] = i[0]
                idx += 1
        else:
            for j in range(int(i[1] / 2)):
                res[idx] = i[0]
                res[len(res) - idx - 1] = i[0]
                idx += 1
            res[int(len(res) / 2)] = i[0]

    for i in res:
        print(i, end='')


if __name__ == "__main__":
    solution()
