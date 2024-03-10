# BOJ_10799
# 쇠막대기

import sys


def solution():
    arr = sys.stdin.readline().strip()
    cur_stick = 0
    res = 0
    for i in range(len(arr)):
        if arr[i] == ')':
            cur_stick -= 1
            if arr[i - 1] == '(':
                res += cur_stick
        else:
            cur_stick += 1
            if arr[i + 1] != ')':
                res += 1
    
    print(res)


if __name__ == "__main__":
    solution()
