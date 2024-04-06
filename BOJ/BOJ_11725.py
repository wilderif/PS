# BOJ_11725
# 트리의 부모 찾기

import sys


def main():
    n = int(sys.stdin.readline())
    arr = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    res = [0 for _ in range(n + 1)]
    stack = list()
    stack.append(1)
    res[1] = -1
    while stack:
        cur = stack.pop()
        for i in arr[cur]:
            if res[i] == 0:
                res[i] = cur
                stack.append(i)
    
    for i in range(2, n + 1):
        print(res[i])


if __name__ == "__main__":
    main()
