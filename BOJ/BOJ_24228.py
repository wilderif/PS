# BOJ_24228
# 젓가락

import sys

inp = sys.stdin.readline


def main():
    n, r = map(int, inp().split())
    print(n + r * 2 - 1)


if __name__ == "__main__":
    main()
