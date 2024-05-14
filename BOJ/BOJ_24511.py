# BOJ_24511
# queuestack

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    a = list(map(int, inp().split()))
    b = list(map(int, inp().split()))
    m = int(inp())
    c = list(map(int, inp().split()))
    
    cnt = m
    for i in range(n - 1, -1, -1):
        if not a[i] and cnt:
            print(b[i], end= ' ')
            cnt -= 1
            if cnt == 0:
                return
    idx = 0
    while cnt:
        print(c[idx], end=' ')
        idx += 1
        cnt -= 1


if __name__ == "__main__":
    main()
