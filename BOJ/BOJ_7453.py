# BOJ_7453
# 합이 0인 네 정수

import sys


def main():
    n = int(sys.stdin.readline())
    a, b, c, d = [], [], [], []
    for _ in range(n):
        t1, t2, t3, t4 = map(int, sys.stdin.readline().split())
        a.append(t1)
        b.append(t2)
        c.append(t3)
        d.append(t4)

    dictionary = {}
    for i in a:
        for j in b:
            tmp = i + j
            dictionary[tmp] = dictionary.get(tmp, 0) + 1

    res = 0
    for i in c:
        for j in d:
            tmp = -(i + j)
            res += dictionary.get(tmp, 0)
    print(res)

    # n = int(sys.stdin.readline())
    # arr = []
    # for _ in range(n):
    #     arr.append(list(map(int, sys.stdin.readline().split())))
    
    # arr_1 = []
    # arr_2 = []
    # for i in range(n):
    #     for j in range(n):
    #         arr_1.append(arr[i][0] + arr[j][1])
    #         arr_2.append(arr[i][2] + arr[j][3])
    # arr_1.sort()
    # arr_2.sort(reverse=True)

    # idx_1 = 0
    # idx_2 = 0
    # res = 0
    # while idx_1 < n * n and idx_2 < n * n:
    #     cur = arr_1[idx_1] + arr_2[idx_2]
    #     if cur < 0:
    #         idx_1 += 1
    #     elif cur == 0:
    #         tmp_1 = arr_1[idx_1]
    #         cnt_1 = 0
    #         while idx_1 < n * n:
    #             if arr_1[idx_1] == tmp_1:
    #                 cnt_1 += 1
    #                 idx_1 += 1
    #             else:
    #                 break

    #         tmp_2 = arr_2[idx_2]
    #         cnt_2 = 0
    #         while idx_2 < n * n:
    #             if arr_2[idx_2] == tmp_2:
    #                 cnt_2 += 1
    #                 idx_2 += 1
    #             else:
    #                 break
    #         res += cnt_1 * cnt_2
    #     else:
    #         idx_2 += 1

    # print(res)


if __name__ == "__main__":
    main()
