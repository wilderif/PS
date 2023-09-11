# BOJ_1789
# 수들의 합

def solution():
    n = int(input())
    res = 0
    cnt = 0

    for i in range(1, n + 1):
        res += i
        if res > n:
            break
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    solution()
