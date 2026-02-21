# BOJ_26570
# Semiperfect

import sys
import itertools

inp = sys.stdin.readline


def solution(m):
    divisors = [1]
    for i in range(2, int(m ** (1 / 2)) + 1):
        if m % i:
            continue
        divisors.append(i)
        if i != m // i:
            divisors.append(m // i)

    for i in range(2, len(divisors) + 1):
        for j in itertools.combinations(divisors, i):
            if sum(j) == m:
                return "Semiperfect"

    return "NOT Semiperfect"


def main():
    n = int(inp())
    for _ in range(n):
        m = int(inp())
        print(solution(m))


if __name__ == "__main__":
    main()
