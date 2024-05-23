# BOJ_14890
# 경사로

import sys

inp = sys.stdin.readline

def check(target):
    used = [False for _ in range(n)]

    for i in range(n - 1):
        if target[i] == target[i + 1]:
            continue
        elif target[i] - 1 == target[i + 1]:
            if i + l >= n:
                return False
            tmp_idx = i + 1
            for j in range(l - 1):
                if target[tmp_idx + j] != target[tmp_idx + j + 1]:
                    return False
                used[tmp_idx + j] = True
            used[tmp_idx + l - 1] = True
        elif target[i] + 1 == target[i + 1]:
            match = target[i]
            for j in range(l):
                if i - j < 0 or target[i - j] != match or used[i - j]:
                    return False
        else:
            return False
    return True    


def main():
    global n, l
    n, l = map(int, inp().split())
    arr = [list(map(int, inp().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        tmp_arr = list(arr[j][i] for j in range(n))
        if check(arr[i]):
            res += 1
        if check(tmp_arr):
            res += 1
    print(res)
                
    
if __name__ == "__main__":
    main()
