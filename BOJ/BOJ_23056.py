# BOJ_23056
# 참가자 명단

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    arr = [[] for _ in range(n)]
    while True:
        a, b = inp().split()
        if a == "0" and b == "0":
            break
        a = int(a)
        if len(arr[a - 1]) < m:
            arr[a - 1].append(b)
    
    for a in arr:
        a.sort(key=lambda x: (len(x), x))

    for i in range(0, n, 2):
        for j in range(m):
            if j >= len(arr[i]):
                break
            print(i + 1, arr[i][j])
    for i in range(1, n, 2):
        for j in range(m):
            if j >= len(arr[i]):
                break
            print(i + 1, arr[i][j])


if __name__ == "__main__":
    main()
