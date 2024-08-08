# BOJ_2872
# 우리집엔 도서관이 있어

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = [int(inp()) for _ in range(n)]
    target = n
    for i in range(n - 1, -1, -1):
        if arr[i] == target:
            target -= 1
    print(target)
    


if __name__ == "__main__":
    main()
