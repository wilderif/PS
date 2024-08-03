# BOJ_17254
# 키보드 이벤트

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = []
    for _ in range(m):
        a, b, c = inp().split()
        arr.append((int(a), int(b), c))
    arr.sort(key=lambda x: (x[1], x[0]))

    for i in arr:
        print(i[2], end='')


if __name__ == "__main__":
    main()
