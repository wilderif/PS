# BOJ_14655
# 욱제는 도박쟁이야!!

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr1 = list(map(int, inp().split()))
    arr2 = list(map(int, inp().split()))
    for i in range(n):
        if arr1[i] < 0:
            arr1[i] = -arr1[i]
        if arr2[i] > 0:
            arr2[i] = -arr2[i]
    
    print(sum(arr1) - sum(arr2))


if __name__ == "__main__":
    main()
