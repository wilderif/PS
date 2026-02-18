# BOJ_14919
# 분포표 만들기

import sys

inp = sys.stdin.readline


def main():
    m = int(inp())
    arr = [0 for _ in range(m)]
    for num in map(float, inp().split()):
        arr[int(num * m + 1e-12)] += 1
    print(*arr)


if __name__ == "__main__":
    main()
