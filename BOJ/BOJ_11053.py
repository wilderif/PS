# BOJ_11053
# 가장 긴 증가하는 부분 수열

import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    mem = [1 for _ in range(n)]

    for i in range(n):
        tmp = 0
        for j in range(i): 
            if arr[j] < arr[i]:
                tmp = max(tmp, mem[j])
        mem[i] += tmp
    print(max(mem))

    
if __name__ == "__main__":
    main()
