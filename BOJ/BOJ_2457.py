# BOJ_2457
# 공주님의 정원

import sys


def main():
    n = int(sys.stdin.readline())
    arr = list()
    month = list(0 for _ in range(13))
    for i in range(1, 13):
        if i == 4 or i == 6 or i == 9 or i == 11:
            month[i] += month[i - 1] + 30
        elif i == 2:
            month[i] += month[i - 1] + 28
        else:
            month[i] += month[i - 1] + 31
    
    for _ in range(n):
        a, b, c, d = map(int, sys.stdin.readline().split())
        tmp_s = month[a - 1] + b
        tmp_e = month[c - 1] + d
        arr.append((tmp_s, tmp_e))
    arr.sort(key=lambda x:(x[0], x[1]))
    
    target_s = month[2] + 1
    target_e = month[11]
    res = list()
    cur_end = target_s
    idx = 0
    while idx < n:
        if arr[idx][1] <= target_s:
            idx += 1
            continue
        if arr[idx][0] > target_e:
            break
        if arr[idx][0] > cur_end:
            break
        else:
            cur_max = 0
            res.append(cur_max)
            while idx < n and arr[idx][0] <= cur_end:
                cur_max = max(cur_max, arr[idx][1])
                res[-1] = cur_max
                idx += 1
            cur_end = cur_max
            if cur_end > target_e:
                break

    if cur_end <= target_e:
        print(0)
    else:
        print(len(res))
    

if __name__ == "__main__":
    main()
