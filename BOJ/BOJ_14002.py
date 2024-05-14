# BOJ_14002
# 가장 긴 증가하는 부분 수열 4

import sys


def main():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    mem = [[1, -1] for _ in range(n)]
    cur_max, max_idx = 1, 0
    for i in range(n):
        tmp = 0
        tmp_idx = -1
        for j in range(i): 
            if arr[j] < arr[i]:
                if mem[j][0] > tmp:
                    tmp_idx = j
                    tmp = mem[j][0]
        mem[i][0] += tmp
        mem[i][1] = tmp_idx
        if mem[i][0] > cur_max:
            cur_max = mem[i][0]
            max_idx = i
    print(cur_max)
    path = list()
    while max_idx != -1:
        path.append(arr[max_idx])
        max_idx = mem[max_idx][1]
    print(*path[::-1])

    
if __name__ == "__main__":
    main()
