# BOJ_9466
# 텀 프로젝트

import sys
sys.setrecursionlimit(10**6)


def dfs(arr, check, cycle, i):
    global res
    check[i] = True
    cycle.append(i)

    if check[arr[i]]:
        if arr[i] in cycle:
            tmp = 0
            for j in range(len(cycle)):
                if cycle[j] == arr[i]:
                    tmp = j
                    break
            res -= len(cycle[tmp:])
    else:
        dfs(arr, check, cycle, arr[i])
        

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        arr = [0] + arr
        check = [False for _ in range(n + 1)]
        global res
        res = n
    
        for i in range(1, n + 1):
            if check[i]:
                continue
            else:
                cycle = list()
                dfs(arr, check, cycle, i)

        print(res)
            

if __name__ == "__main__":
    main()
