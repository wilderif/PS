# BOJ_2529
# 부등호

import sys

inp = sys.stdin.readline


def backtracking(idx):
    global res, check
    if idx == k + 1:
        check = True
        if res[0] is None:
            res[0] = list(out)
        else:
            res[1] = list(out)
        return
    
    if idx == 0:
        for i in range(10):
            used[i] = True
            out[idx] = i
            backtracking(idx + 1)
            used[i] = False
    else:
        if arr[idx] == '<':
            for i in range(out[idx - 1] + 1, 10):
                if not used[i]:
                    used[i] = True
                    out[idx] = i
                    backtracking(idx + 1)
                    used[i] = False
        else:
            for i in range(out[idx - 1]):
                if not used[i]:
                    used[i] = True
                    out[idx] = i
                    backtracking(idx + 1)
                    used[i] = False


def main():
    global k, arr, used, out, res, check
    k = int(inp())
    arr = [None] + list(inp().split())
    used = [False for _ in range(10)]
    out = [None for _ in range(k + 1)]

    res = [None, None]
    check = False
    for i in range(10):
        if check:
            break
        out[0] = i
        used[i] = True
        backtracking(1)
        used[i] = False

    check = False
    for i in range(9, -1, -1):
        if check:
            break
        out[0] = i
        used[i] = True
        backtracking(1)
        used[i] = False
    
    print("".join(map(str, res[1])))
    print("".join(map(str, res[0])))


if __name__ == "__main__":
    main()
