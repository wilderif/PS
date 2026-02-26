# BOJ_30614
# Port Robot

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(inp().rstrip())
    stack = []
    for c in arr:
        if c.islower():
            stack.append(c)
        else:
            if not stack:
                print(0)
                return
            else:
                if stack[-1].upper() == c:
                    stack.pop()
                else:
                    print(0)
                    return
    if stack:
        print(0)
        return
    print(1)


if __name__ == "__main__":
    main()
