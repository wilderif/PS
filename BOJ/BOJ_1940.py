# BOJ_1940
# 주몽

def solution():
    n = int(input())
    m = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == m:
                res += 1
    print(res)


if __name__ == "__main__":
    solution()
