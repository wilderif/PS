# BOJ_1305
# 광고

import sys

inp = sys.stdin.readline


def failure(s):
    f = [0 for _ in range(len(s))]
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    return f


def main():
    l = int(inp())
    s = inp().rstrip()

    print(l - failure(s)[l - 1]) 


if __name__ == "__main__":
    main()
