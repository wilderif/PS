# BOJ_2485
# 가로수

import sys


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def main():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    dis = []
    for i in range(1, n):
        dis.append(arr[i] - arr[i - 1])
    total_gcd = dis[0]
    for i in range(len(dis)):
        total_gcd = gcd(total_gcd, dis[i])
    res = 0
    for i in range(1, n):
        res += (arr[i] - arr[i - 1]) // total_gcd - 1
    print(res)


if __name__ == "__main__":
    main()
