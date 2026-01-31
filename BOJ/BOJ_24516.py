# BOJ_24516
# 잘 알려진 수열 구하기

import sys

inp = sys.stdin.readline


def main():
    print(*[i * 2 + 1 for i in range(int(inp()))])


if __name__ == "__main__":
    main()
