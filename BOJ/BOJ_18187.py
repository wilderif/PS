# BOJ_18187
# 평면 분할


def solution():
    n = int(input())
    arr = [0 for _ in range(n + 1)]
    arr[0] = 1
    for i in range(1, n + 1):
        arr[i] = arr[i - 1] + i - (i - 1) // 3
    print(arr[n])


if __name__ == "__main__":
    solution()
