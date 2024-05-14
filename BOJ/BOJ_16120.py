# BOJ_16120
# PPAP

import sys


def solution():
    s = sys.stdin.readline().rstrip()
    stack = []

    for i in s:
        stack.append(i)
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ['P']:
        print("PPAP")
    else:
        print("NP")


if __name__ == "__main__":
    solution()
