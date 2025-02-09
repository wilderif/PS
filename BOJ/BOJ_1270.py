# BOJ_1270
# 전쟁 - 땅따먹기

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    for _ in range(n):
        t, *arr = list(map(int, inp().split()))
        if t == 0:
            print("SYJKGW")
            continue
        if t == 1:
            print(arr[0])
            continue

        cntMap = {}
        for el in arr:
            cntMap[el] = cntMap.get(el, 0) + 1

        cntMap = sorted(cntMap.items(), key=lambda x: x[1], reverse=True)
        if cntMap[0][1] >= t // 2 + 1:
            print(cntMap[0][0])
        else:
            print("SYJKGW")


if __name__ == "__main__":
    main()
