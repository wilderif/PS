# BOJ_1644
# 소수의 연속합

import sys


def main():
    n = int(sys.stdin.readline())
    prime = [True for _ in range(n + 1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if prime[i]:
            j = i
            while i * j < n + 1:
                prime[i * j] = False
                j += 1

    prime_remain = [0]
    for i in range(2, n + 1):
        if prime[i]:
            prime_remain.append(i)
    
    idx_1, idx_2 = 0, 0
    res = 0
    cur = prime_remain[idx_1]
    while idx_2 < len(prime_remain):
        if idx_1 == idx_2 or cur <= n:
            if cur == n:
                res += 1
            if idx_2 == len(prime_remain) - 1:
                break
            idx_2 += 1
            cur += prime_remain[idx_2]
        else:
            cur -= prime_remain[idx_1]
            idx_1 += 1
    print(res)


if __name__ == "__main__":
    main()
