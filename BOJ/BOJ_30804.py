# BOJ_30804
# 과일 탕후루

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    arr2 = []
    cur = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            cnt += 1
        else:
            arr2.append((cur, cnt))
            cur = arr[i]
            cnt = 1
    arr2.append((cur, cnt))
    
    cnt = {}
    for i in range(10):
        cnt[i] = 0
    res, cur = 0, 0
    p1, p2 = 0, 0
    while p1 < len(arr2):
        if cnt[0] < 3 and p2 < len(arr2):
            if not cnt[arr2[p2][0]]:
                cnt[0] += 1
            cnt[arr2[p2][0]] += 1
            cur += arr2[p2][1]
            p2 += 1
        else:
            cnt[arr2[p1][0]] -= 1
            if not cnt[arr2[p1][0]]:
                cnt[0] -= 1
            cur -= arr2[p1][1]
            p1 += 1
        if cnt[0] <= 2:
            res = max(res, cur)

    print(res)


if __name__ == "__main__":
    main()
