# BOJ_27172
# 수 나누기 게임

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    max_length = max(arr) + 1
    res = dict()
    for i in arr:
        res[i] = 0

    for i in arr:
        j = 2
        while i * j < max_length:
            if i * j in res:
                res[i] += 1
                res[i * j] -= 1
            j += 1
    
    for i in arr:
        print(res[i], end=" ")
    

if __name__ == "__main__":
    main()
