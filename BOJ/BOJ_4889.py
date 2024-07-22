# BOJ_4889
# 안정적인 문자열

import sys

inp = sys.stdin.readline


def main():
    case = 1
    while True:
        s = inp().rstrip()
        if s[0] == '-':
            break
        stack = []
        for c in s:
            if c == '{':
                stack.append(c)
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
        res = 0
        while stack:
            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
            stack.pop()
            res += 1
        print(case, end=". ")
        print(res)
        case += 1


if __name__ == "__main__":
    main()
