# BOJ_16287
# Parcel

import sys

inp = sys.stdin.readline


def main():
    w, n = map(int, inp().split())
    arr = list(map(int, inp().split()))
    check = [False for _ in range(w)]

    for i in range(1, n - 2):
        for j in range(i):
            if arr[i] + arr[j] < w:
                check[arr[i] + arr[j]] = True
        for j in range(i + 2, n):
            if arr[i + 1] + arr[j] < w and check[w - arr[i + 1] - arr[j]]:
                print("YES")
                return
    print("NO")

        
if __name__ == "__main__":
    main()
