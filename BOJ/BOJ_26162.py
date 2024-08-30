# BOJ_26162
# 인공 원소

import sys

inp = sys.stdin.readline


def main():
    prime = [False, False] + [True for _ in range(117)]
    for i in range(2, int(118 ** (1 / 2)) + 1):
        if prime[i]:
            for j in range(2, 118):
                if i * j > 118:
                    break
                prime[i * j] = False
    n = int(inp())
    for _ in range(n):
        a = int(inp())
        for i in range(1, a // 2 + 1):
            if prime[i] and prime[a - i]:
                print("Yes")
                break
        else:
            print("No")


if __name__ == "__main__":
    main()
