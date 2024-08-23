# BOJ_2590
# 색종이

import sys

inp = sys.stdin.readline


def main():
    arr = [0]
    for _ in range(6):
        arr.append(int(inp()))
    res = 0
    res += arr[6]
    
    res += arr[5]
    arr[1] = max(arr[1] - arr[5] * 11, 0)
    
    res += arr[4]
    if arr[2] > arr[4] * 5:
        arr[2] -= arr[4] * 5
    elif arr[2] == arr[4] * 5:
        arr[2] = 0
    else:
        remain = 20 * arr[4]
        remain -= arr[2] * 4
        arr[1] = max(arr[1] - remain, 0)
        arr[2] = 0
    
    if arr[3] % 4:
        res += arr[3] // 4 + 1
        if arr[3] % 4 == 1:
            if arr[2] > 5:
                arr[1] = max(arr[1] - 7, 0)
                arr[2] -= 5
            else:
                arr[1] = max(arr[1] - (36 - 9 - arr[2] * 4), 0)
                arr[2] = 0
        if arr[3] % 4 == 2:
            if arr[2] > 3:
                arr[1] = max(arr[1] - 6, 0)
                arr[2] -= 3
            else:
                arr[1] = max(arr[1] - (36 - 18 - arr[2] * 4), 0)
                arr[2] = 0
        if arr[3] % 4 == 3:
            if arr[2] > 1:
                arr[1] = max(arr[1] - 5, 0)
                arr[2] -= 1
            else:
                arr[1] = max(arr[1] - (36 - 27 - arr[2] * 4), 0)
                arr[2] = 0
    else:
        res += arr[3] // 4

    if arr[2] % 9:
        res += arr[2] // 9 + 1
        arr[1] = max(arr[1] - (36 - (arr[2] % 9) * 4), 0)
    else:
        res += arr[2] // 9

    if arr[1] % 36:
        res += arr[1] // 36 + 1
    else:
        res += arr[1] // 36

    print(res)


if __name__ == "__main__":
    main()
