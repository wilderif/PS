# BOJ_11727
# 2×n 타일링 2

def solution():
    n = int(input())
    mem = [0 for _ in range(1001)]
    mem[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:
            mem[i] = mem[i - 1] * 2 + 1
        else:
            mem[i] = mem[i - 1] * 2 - 1

    print(mem[n] % 10007)


if __name__ == "__main__":
    solution()
