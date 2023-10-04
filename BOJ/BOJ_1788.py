# BOJ_1788
# 피보나치 수의 확장

def solution():
    n = int(input())

    if n == 0:
        print(0)
    elif n > 0 or (-n) % 2 == 1:
        print(1)
    else:
        print(-1)

    if n < 0:
        n = -n

    mem = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            mem[i] = 1
        else:
            mem[i] = mem[i - 2] + mem[i - 1]
            mem[i] %= 1000000000

    print(mem[n])


if __name__ == "__main__":
    solution()
