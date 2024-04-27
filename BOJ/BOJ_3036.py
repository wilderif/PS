# BOJ_3036
# 링

import sys

inp = sys.stdin.readline


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    for i in range(1, n):
        gcd_cur = gcd(arr[0], arr[i])
        print(arr[0] // gcd_cur, end='/')
        print(arr[i] // gcd_cur)
    
        
if __name__ == "__main__":
    main()
