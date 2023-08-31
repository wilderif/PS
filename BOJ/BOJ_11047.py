# BOJ_11047
# 동전 0

def solution():
    n, k = map(int, input().split())
    coin_type = list()
    count = 0

    for _ in range(n):
        coin_type.append(int(input()))

    for i in range(n - 1, -1, -1):
        if coin_type[i] > k:
            continue
        else:
            count += k // coin_type[i]
            k = k % coin_type[i]

    print(count)


if __name__ == "__main__":
    solution()
