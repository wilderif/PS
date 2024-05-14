# BOJ_11723
# 집합

import sys


def solution():
    def excution(inst, x, s):
        if inst == "add":
            if x not in s:
                s.append(x)
        elif inst == "remove":
            if x in s:
                s.remove(x)
        elif inst == "check":
            if x not in s:
                print(0)
            else:
                print(1)
        elif inst == "toggle":
            if x not in s:
                s.append(x)
            else:
                s.remove(x)
        elif inst == "all":
            s = [j for j in range(1, 21)]
        elif inst == "empty":
            s = []
        return s

    set_arr = []
    m = int(sys.stdin.readline())

    for i in range(m):
        a = list(sys.stdin.readline().split())
        if len(a) == 2:
            set_arr = excution(a[0], int(a[1]), set_arr)
        else:
            set_arr = excution(a[0], -1, set_arr)


if __name__ == "__main__":
    solution()
