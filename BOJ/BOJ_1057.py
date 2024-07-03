# BOJ_1057
# 토너먼트

import sys

inp = sys.stdin.readline


def main():
    n, a, b = map(int, inp().split())
    res = 1
    while True:
        if a % 2 and a + 1 == b:
            break
        if b % 2 and b + 1 == a:
            break
        a = (a + 1) // 2
        b = (b + 1) // 2
        res += 1

    print(res)
 

if __name__ == "__main__":
    main()
