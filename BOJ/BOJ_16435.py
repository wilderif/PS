# BOJ_16435
# 스네이크버드

import sys

inp = sys.stdin.readline


def main():
    n, l = map(int, inp().split())
    h = list(map(int, inp().split()))
    h.sort()
    for i in range(len(h)):
        if h[i] <= l:
            l += 1
        else:
            break
    print(l)

    
if __name__ == "__main__":
    main()
