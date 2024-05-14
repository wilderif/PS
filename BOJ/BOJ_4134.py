# BOJ_4134
# 다음 소수

import sys
inp = sys.stdin.readline


def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    else:
        return True


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        while not prime(n):
            n += 1
        print(n)


if __name__ == "__main__":
    main()
