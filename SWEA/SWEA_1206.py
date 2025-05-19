# SWEA_1206
# [S/W 문제해결 기본] 1일차 - View

for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(2, n - 2):
        tmp = 0
        for j in range(1, 3):
            tmp = max(arr[i - j], arr[i + j], tmp)
        res += arr[i] - tmp if arr[i] > tmp else 0
    print(f"#{t + 1}", res)
