# BOJ_2568
# 전깃줄 - 2

import sys
import bisect


def main():
    n = int(input())
    arr = []
    dic = {}
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        arr.append((a, b))
        dic[arr[i][1]] = arr[i][0]
    arr.sort(key=lambda x:x[0])

    res = []
    idx = []
    for i in range(n):
        target = arr[i][1]
        if not res or res[-1] < target:
            idx.append((len(res), target))
            res.append(target)
        else:
            target_idx = bisect.bisect_left(res, target)
            res[target_idx] = target
            idx.append((target_idx, target))

    target = len(res) - 1
    for i in range(n - 1, -1, -1):
        if idx[i][0] == target:
            dic.pop(idx[i][1])
            target -= 1

    res_idx = list(dic.values())
    res_idx.sort()
    print(n - len(res))
    for i in res_idx:
        print(i)


if __name__ == "__main__":
    main()
