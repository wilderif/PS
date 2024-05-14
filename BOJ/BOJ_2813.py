# BOJ_2813
# 매력있는 울타리

import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())
    arr_1 = list(map(int, sys.stdin.readline().split()))
    arr_2 = list(map(int, sys.stdin.readline().split()))

    # 위로 peak = 1, 아래로 peak = -1
    # side 일 경우 2, -2
    # 감소 상태 -3, 증가 상태 3
    check_arr = [0 for _ in range(n)]

    # 증가 감소 상태
    flag = True
    for i in range(n - 1):
        # 증가로 전환
        if arr_1[i] < arr_1[i + 1] and flag is False:
            check_arr[i] = -1
            flag = True
        # 감소로 전환
        elif arr_1[i] > arr_1[i + 1] and flag is True:
            check_arr[i] = 1
            flag = False
        # 감소 상태
        elif flag is False:
            check_arr[i] = -3
        # 증가 상태
        elif flag is True:
            check_arr[i] = 3

    # side check
    if arr_1[0] > arr_1[1]:
        check_arr[0] = 2
    else:
        check_arr[0] = -2
    if flag is False:
        check_arr[n - 1] = -2
    else:
        check_arr[n - 1] = 2

    arr_2 = deque(sorted(arr_2))

    res_arr = [0 for _ in range(n)]
    # peak 채우기
    for i in range(1, n - 1):
        if check_arr[i] == -1:
            res_arr[i] = arr_2.popleft()
        elif check_arr[i] == 1:
            res_arr[i] = arr_2.pop()

    # side 채우기
    if check_arr[0] == 2 and arr_2:
        res_arr[0] = arr_2.pop()
    elif check_arr[0] == -2 and arr_2:
        res_arr[0] = arr_2.popleft()
    if check_arr[n - 1] == 2 and arr_2:
        res_arr[n - 1] = arr_2.pop()
    elif check_arr[n - 1] == -2 and arr_2:
        res_arr[n - 1] = arr_2.popleft()

    # 나머지 채우기
    for i in range(1, n - 1):
        if check_arr[i] == -3:
            res_arr[i] = arr_2.pop()
        elif check_arr[i] == 3:
            res_arr[i] = arr_2.popleft()

    res = 0
    for i in range(n - 1):
        res += abs(res_arr[i] - res_arr[i + 1])

    print(res)
    for i in res_arr:
        print(i, end=' ')


if __name__ == "__main__":
    solution()
