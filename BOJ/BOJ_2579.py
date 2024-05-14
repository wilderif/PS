# BOJ_2579
# 계단 오르기

def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    if n < 3:
        print(sum(arr))
    else:
        mem = [0 for _ in range(n)]
        mem[0] = arr[0]
        mem[1] = arr[0] + arr[1]
        mem[2] = max(arr[0] + arr[2], arr[1] + arr[2])
        for i in range(3, n):
            mem[i] = max(mem[i - 2] + arr[i], mem[i - 3] + arr[i - 1] + arr[i])
        print(mem[n - 1])


if __name__ == "__main__":
    solution()
