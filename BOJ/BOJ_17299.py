# BOJ_17299
# 오등큰수

import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    count = [0 for _ in range(1000001)]
    for i in arr:
        count[i] += 1

    stack = []
    res = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        while stack and count[stack[-1]] <= count[arr[i]]:
            stack.pop()
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(arr[i])

    print(*res)


if __name__ == "__main__":
    main()
