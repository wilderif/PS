# BOJ_2776
# 암기왕

import sys

inp = sys.stdin.readline


def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = set(map(int, inp().split()))
        m = int(inp())
        target = list(map(int, inp().split()))
        for num in target:
            if num in arr:
                print(1)
            else:
                print(0)
    

if __name__ == "__main__":
    main()
