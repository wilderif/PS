# BOJ_3687
# 성냥개비

import sys


def solution():
    def biggest(x):
        res = ''
        if x % 2 == 0:
            res += '1' * (x // 2)
        else:
            res += '7'
            x -= 3
            res += '1' * (x // 2)
        return res

    mem = [-1 for _ in range(101)]
    mem[2] = '1'
    mem[3] = '7'
    mem[4] = '4'
    mem[5] = '2'
    mem[6] = '0'
    mem[7] = '8'
    for i in range(8, 101):
        if i % 7 == 0:
            mem[i] = mem[7] + mem[i - 7]
        elif i % 7 <= 2:
            mem[i] = mem[2] + mem[i - 2]
        elif i % 7 <= 4:
            mem[i] = mem[5] + mem[i - 5]
        elif i % 7 <= 6:
            mem[i] = mem[6] + mem[i - 6]
    mem[6] = '6'
    for i in range(8, 101):
        if mem[i][:2] == '00':
            mem[i] = '28' + mem[i][2:]
        elif mem[i][0] == '0':
            mem[i] = '6' + mem[i][1:]

    n = int(sys.stdin.readline())
    for _ in range(n):
        a = int(sys.stdin.readline())
        print(int(mem[a]), end=' ')
        print(biggest(a))


if __name__ == "__main__":
    solution()
