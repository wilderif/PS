# BOJ_14003
# 가장 긴 증가하는 부분 수열 5

import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    arr = [int(i) for i in sys.stdin.readline().split()]
    check = [arr[0]]
    idx = []
    for i in range(n):
        if check[-1] < arr[i]:
            idx.append(len(check))
            check.append(arr[i])
        else:
            tmp = bisect.bisect_left(check, arr[i])
            idx.append(tmp)
            check[tmp] = arr[i]
    
    res = [0 for _ in range(len(check))]
    target = len(check) - 1
    for i in range(n - 1, -1, -1):
        if idx[i] == target:
            res[target] = arr[i]
            target -= 1        

    print(len(check))
    print(*res)


if __name__ == "__main__":
    main()
