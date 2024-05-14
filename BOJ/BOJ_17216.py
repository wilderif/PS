# BOJ_17216
# 가장 큰 감소 부분 수열

import sys


def main():
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    mem = [i for i in arr]
    
    for i in range(n):
        cur = 0
        for j in range(i):
            if arr[i] < arr[j]:
                cur = max(cur, mem[j])
        mem[i] += cur
    print(max(mem))


if __name__ == "__main__":
    main()
