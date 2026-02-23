# BOJ_14376
# The Last Word (Large)

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for i in range(t):
        print(f"Case #{i + 1}: ", end="")
        s = inp().rstrip()
        res = s[0]
        for c in s[1:]:
            if c >= res[0]:
                res = c + res
            else:
                res += c
        print(res)


if __name__ == "__main__":
    main()
