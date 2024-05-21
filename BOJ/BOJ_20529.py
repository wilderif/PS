# BOJ_20529
# 가장 가까운 세 사람의 심리적 거리

import sys

inp = sys.stdin.readline


def difference(str_1, str_2):
    tmp = 0
    for i in range(4):
        if str_1[i] != str_2[i]:
            tmp += 1
    return tmp
    

def main():
    t = int(inp())
    for _ in range(t):
        n = int(inp())
        arr = list(inp().split())
        if n > 32:
            print(0)
            continue
        res = 12
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    tmp = difference(arr[i], arr[j])
                    tmp += difference(arr[j], arr[k])
                    tmp += difference(arr[k], arr[i])
                    res = min(res, tmp)
        print(res)
                
    
if __name__ == "__main__":
    main()
