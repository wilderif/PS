# BOJ_16499
# 동일한 단어 그룹화하기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    s = set()
    for _ in range(n):
        s.add("".join(sorted(list(inp().strip()))))
    print(len(s))


if __name__ == "__main__":
    main()
