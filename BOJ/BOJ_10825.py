# BOJ_10825
# 국영수

import sys


def main():
    n = int(input())
    arr = list()
    for _ in range(n):
        tmp = list(sys.stdin.readline().split())
        for i in range(1, 4):
            tmp[i] = int(tmp[i])
        arr.append(tmp)
    arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    for i in range(n):
        print(arr[i][0])

    
if __name__ == "__main__":
    main()
