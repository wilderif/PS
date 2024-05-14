# BOJ_2161
# 카드1

def solution():
    n = int(input())
    arr = [i for i in range(1, n + 1)]

    while arr:
        print(arr.pop(0), end=' ')
        if arr:
            tmp = arr[0]
            arr = arr[1:]
            arr.append(tmp)


if __name__ == "__main__":
    solution()
