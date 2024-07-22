# BOJ_1935
# 후위 표기식2

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    s = inp().rstrip()
    dic = {}
    cur = ord("A")
    for _ in range(n):
        dic[chr(cur)] = int(inp())
        cur += 1
    stack = []
    for c in s:
        if c not in ('+', '-', '*', '/'):
            stack.append(dic[c])
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        if c == '-':
            stack.append(-(stack.pop() - stack.pop()))
        if c == '*':
            stack.append(stack.pop() * stack.pop())
        if c == '/':
            stack.append(1 / (stack.pop() / stack.pop()))
    print(f"{stack[0]:.2f}")


if __name__ == "__main__":
    main()
