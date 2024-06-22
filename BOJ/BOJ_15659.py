# BOJ_15659
# 연산자 끼워넣기 (3)

import sys

inp = sys.stdin.readline


def oper(arr, seq):
    global max_res, min_res
    ret = 0
    pn = True
    tmp = arr[0]
    for i in range(n - 1):
        if seq[i] <= 1:
            if pn:
                ret += tmp
            else:
                ret -= tmp
            tmp = arr[i + 1]
            if seq[i] == 0:
                pn = True
            else:
                pn = False
        else:
            if seq[i] == 2:
                tmp *= arr[i + 1]
            else:
                tmp //= arr[i + 1]
    if pn:
        ret += tmp
    else:
        ret -= tmp
    max_res = max(max_res, ret)
    min_res = min(min_res, ret)
    

def backtracking(opp, vis, seq, arr, depth):
    if depth == n - 1:
        oper(arr, seq)
    for i in range(4):
        if vis[i] < opp[i]:
            vis[i] += 1
            seq[depth] = i
            backtracking(opp, vis, seq, arr, depth + 1)
            vis[i] -= 1


def main():
    global n, max_res, min_res
    n = int(inp())
    arr = list(map(int, inp().split()))
    opp = list(map(int, inp().split()))
    vis = [0 for _ in range(4)]
    seq = [0 for _ in range(n - 1)]
    max_res = -(10 ** 10)
    min_res = 10 ** 10
    backtracking(opp, vis, seq, arr, 0)
    print(max_res)
    print(min_res)


if __name__ == "__main__":
    main()
