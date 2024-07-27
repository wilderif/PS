# BOJ_1138
# 한 줄로 서기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    index = 0
    res = [0 for _ in range(n)]
    for i in range(n):
        target_index = index
        cnt = 0
        while cnt < arr[i]:
            if not res[target_index]:
                cnt += 1
            target_index += 1
        while res[target_index]:
            target_index += 1
        res[target_index] = i + 1
    print(*res)
    
        
if __name__ == "__main__":
    main()
