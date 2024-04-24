# BOJ_13414
# 수강신청

import sys

inp = sys.stdin.readline


def main():
    k, l = map(int, inp().split())
    mapp = {}
    for i in range(l):
        tmp = inp().rstrip()
        mapp[tmp] = i
    
    arr = list(mapp.items())
    arr.sort(key=lambda x:x[1])
    for i in range(k):
        if i == len(arr):
            break
        print(arr[i][0])


if __name__ == "__main__":
    main()
