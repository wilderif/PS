# BOJ_3986
# 좋은 단어

import sys


def solution():
    n = int(sys.stdin.readline())
    res = 0
    for _ in range(n):
        s = sys.stdin.readline().strip()
        stack = list()
        for c in s:
            if stack and stack[len(stack) - 1] == c:
                stack.pop()
            else:
                stack.append(c)
        if not stack:
            res += 1

    print(res)


if __name__ == "__main__":
    solution()
