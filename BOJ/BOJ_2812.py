# BOJ_2812
# 크게 만들기

import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    num = sys.stdin.readline().strip()
    stack = list()
    for i in num:
        while stack and i > stack[-1] and k:
            stack.pop()
            k -= 1
        stack.append(i)

    if k:
        print(''.join(stack[:-k]))
    else:
        print(''.join(stack))


if __name__ == "__main__":
    main()
