# BOJ_10451
# 순열 사이클

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = [0] + list(map(int, inp().split()))
        check = [False for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            if check[i]:
                continue
            res += 1
            cur = i
            while not check[cur]:
                check[cur] = True
                cur = arr[cur]
        print(res)


if __name__ == "__main__":
    main()
