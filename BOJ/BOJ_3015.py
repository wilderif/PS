# BOJ_3015
# 오아시스 재결합

import sys


def main():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]

    stack = []
    res = 0
    for i in arr:
        cur = 1
        while stack and stack[-1][0] <= i:
            if stack[-1][0] < i:
                res += stack[-1][1]
                stack.pop()
            else:
                cur += stack[-1][1]
                res += stack[-1][1]
                stack.pop()
        if stack:
            res += 1
        stack.append((i, cur))
    print(res)


if __name__ == "__main__":
    main()
