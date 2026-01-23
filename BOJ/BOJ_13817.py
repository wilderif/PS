# BOJ_13817
# Everlasting...?

import sys

inp = sys.stdin.readline


def main():
    prime = [False, False, True] + [True, False] * ((10**6) // 2)
    prime_num = [2]
    for i in range(3, len(prime), 2):
        if prime[i]:
            prime_num.append(i)
            for j in range(i * i, len(prime), i):
                prime[j] = False

    def get_key(num):
        prime_set = set()
        for p in prime_num:
            while num % p == 0:
                prime_set.add(p)
                num //= p
            if num == 1:
                break
        return max(prime_set) * 2 - sum(prime_set)

    res = []
    while True:
        a, b = map(int, inp().split())
        if a == 0 and b == 0:
            break
        a_key = get_key(a)
        b_key = get_key(b)
        if a_key > b_key:
            res.append("a")
        else:
            res.append("b")
    print("\n".join(res))


if __name__ == "__main__":
    main()
